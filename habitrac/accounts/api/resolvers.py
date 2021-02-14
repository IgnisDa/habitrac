import ariadne_jwt
from ariadne import MutationType, QueryType
from django.conf import settings
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError

CUSTOM_USER = get_user_model()

auth_type_definitions = [
    ariadne_jwt.jwt_schema,
]

jwt_mutation = MutationType()
jwt_mutation.set_field("tokenAuth", ariadne_jwt.resolve_token_auth)
jwt_mutation.set_field("refreshToken", ariadne_jwt.resolve_refresh)
jwt_mutation.set_field("verifyToken", ariadne_jwt.resolve_verify)

accounts_query = QueryType()
accounts_mutation = MutationType()


@accounts_query.field("userDetails")
@ariadne_jwt.decorators.login_required
def user_details(_, info, **kwargs):
    """ returns basic user data about the currently logged in user """
    if settings.DEBUG:
        import time

        # ? DEBUG: ==>
        # This is here just for testing purposes. We obviously don't want
        # to increase response time in production
        time.sleep(2)
    return {"username": info.context.get("request").user.username}


@accounts_mutation.field("createUser")
def create_user(*_, data, **kwargs):
    """Create a new user using the given `username` and `password` in the `data`
    variable."""
    status = False
    errors = {}
    if CUSTOM_USER.objects.filter(username=data["username"]).exists():
        errors.update(
            {"username": "This username is taken, please choose something else!"}
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
