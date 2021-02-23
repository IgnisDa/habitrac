from ariadne import MutationType, QueryType
from ariadne_token_auth.api import resolvers
from ariadne_token_auth.decorators import login_required
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError

CUSTOM_USER = get_user_model()

auth_type_definitions = [resolvers.type_defs]

auth_mutation = MutationType()
auth_mutation.set_field("getAuthToken", resolvers.get_auth_token)
auth_mutation.set_field("deleteAuthToken", resolvers.delete_auth_token)

accounts_query = QueryType()
accounts_mutation = MutationType()


@accounts_query.field("userProfileDetails")
def user_profile_details(*_, id, **kwargs):
    """ returns basic user data about the user having the specified `id` """
    error = None
    try:
        username = CUSTOM_USER.objects.get(pk=id).username
    except CUSTOM_USER.DoesNotExist:
        username = None
        error = "The requested error does not exist"
    return {"username": username, "error": error}


@accounts_query.field("userDetails")
@login_required
def user_details(_, info, **kwargs):
    """ returns basic user data about the currently logged in user """
    return {"username": info.context.get("request").user.username}


@accounts_mutation.field("createUser")
def create_user(*_, data, **kwargs):
    """Create a new user using the given `username` and `password` in the `data`
    variable."""
    status = False
    errors = {}
    if CUSTOM_USER.objects.filter(username=data["username"]).exists():
        errors.update(
            {"username": ["This username is taken, please choose something else!"]}
        )
    try:
        password_validation.validate_password(data["password"])
    except ValidationError as exc:
        errors.update({"password": list(exc)})
    if not errors:
        errors = None
        CUSTOM_USER.objects.create_user(**data)
        status = True
    return {"status": status, "errors": errors}
