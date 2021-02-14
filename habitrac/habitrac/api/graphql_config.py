import glob

import ariadne
from accounts.api import resolvers as accounts_resolvers
from ariadne.contrib.django.views import GraphQLView
from django.conf import settings
from habits.api import resolvers as habits_resolvers


class HabitracGraphQLView(GraphQLView):
    pass


type_defs = [
    ariadne.load_schema_from_path(f)
    for f in glob.glob(str(settings.BASE_DIR / "*" / "api" / "schema" / "*.graphql"))
]
type_defs.extend(accounts_resolvers.auth_type_definitions)

resolvers = [
    habits_resolvers.query,
    accounts_resolvers.jwt_mutation,
    accounts_resolvers.accounts_query,
    accounts_resolvers.accounts_mutation,
]

schema = ariadne.make_executable_schema(
    type_defs, resolvers, ariadne.snake_case_fallback_resolvers
)
