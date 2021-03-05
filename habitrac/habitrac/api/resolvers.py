from ariadne import QueryType
from django.conf import settings

root_query = QueryType()


@root_query.field("versionCheck")
def version_check(self, info, *args, **kwargs):
    frontend = settings.FRONTEND_VERSION
    backend = settings.BACKEND_VERSION
    return {"frontend": frontend, "backend": backend}
