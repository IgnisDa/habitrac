import ariadne_jwt
from ariadne import MutationType, QueryType

auth_type_definitions = [
    ariadne_jwt.jwt_schema,
]

jwt_mutation = MutationType()
jwt_mutation.set_field("tokenAuth", ariadne_jwt.resolve_token_auth)
jwt_mutation.set_field("refreshToken", ariadne_jwt.resolve_refresh)
jwt_mutation.set_field("verifyToken", ariadne_jwt.resolve_verify)

accounts_query = QueryType()


@accounts_query.field("userDetails")
@ariadne_jwt.decorators.login_required
def user_details(self, info, **kwargs):
    return {"username": info.context.get("request").user.username}
