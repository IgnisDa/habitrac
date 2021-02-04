from django.contrib import admin
from django.urls import path

from habitrac.api.graphql_config import HabitracGraphQLView, schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", HabitracGraphQLView.as_view(schema=schema), name="graphql"),
]
