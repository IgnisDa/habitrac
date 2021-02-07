from django.contrib import admin
from django.urls import path

from habitrac.api import graphql_config

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "graphql/",
        graphql_config.HabitracGraphQLView.as_view(schema=graphql_config.schema),
        name="graphql",
    ),
]
