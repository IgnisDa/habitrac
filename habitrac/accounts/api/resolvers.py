from ariadne import MutationType, QueryType, convert_kwargs_to_snake_case
from ariadne_token_auth.api import resolvers
from ariadne_token_auth.decorators import login_required
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError
from utils.general import get_user
from utils.handlers.errors import ErrorContainer

CUSTOM_USER = get_user_model()

auth_type_definitions = [resolvers.type_defs]

auth_mutation = MutationType()
auth_mutation.set_field("getAuthToken", resolvers.get_auth_token)
auth_mutation.set_field("deleteAuthToken", resolvers.delete_auth_token)

accounts_query = QueryType()
accounts_mutation = MutationType()


@accounts_query.field("userProfileDetails")
@convert_kwargs_to_snake_case
def user_profile_details(*_, username_slug, **kwargs):
    """ returns basic user data about the user having the specified `username_slug` """
    error = None
    try:
        username = CUSTOM_USER.objects.get(username_slug=username_slug).username
    except CUSTOM_USER.DoesNotExist:
        username = None
        error = "The requested user does not exist"
    return {"username": username, "error": error}


@accounts_query.field("userDetails")
@login_required
def user_details(_, info, **kwargs):
    """ returns basic user data about the currently logged in user """
    user = get_user(info)
    return {
        "user": {"username": user.username, "username_slug": user.username_slug},
        "error": None,
    }


@accounts_mutation.field("createUser")
def create_user(*_, data, **kwargs):
    """Create a new user using the given `username` and `password` in the `data`
    variable."""
    error_container = ErrorContainer("identifier", "password")
    status = False
    if CUSTOM_USER.objects.filter(username=data["identifier"]).exists():
        error_container.update_with_error(
            "identifier", "This username is taken, please choose something else!"
        )
    try:
        password_validation.validate_password(data["password"])
    except ValidationError as exc:
        for err in list(exc):
            error_container.update_with_error("password", str(err))
    if not error_container:
        data["username"] = data.pop("identifier")
        CUSTOM_USER.objects.create_user(**data)
        status = True
    return {"status": status, "errors": error_container.get_all_errors()}


@accounts_query.field("getUsersList")
def get_users_list(self, info, *args, **kwargs):
    return CUSTOM_USER.objects.values("username", "username_slug")


@accounts_query.field("getUserReport")
@login_required
def get_user_report(self, info, *args, **kwargs):
    return get_user(info).get_report()


@accounts_mutation.field("setVaultPassword")
@login_required
def set_vault_password(self, info, password, *args, **kwargs):
    user = get_user(info)
    status = False
    error = None
    if not user.vault_password:
        user.set_vault_password(password)
        status = True
    else:
        error = "You have already set a vault password"
    return {"status": status, "error": error}
