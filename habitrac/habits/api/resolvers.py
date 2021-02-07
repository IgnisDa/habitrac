from ariadne import MutationType, QueryType, convert_kwargs_to_snake_case
from ariadne_jwt.decorators import login_required

query = QueryType()
mutation = MutationType()
