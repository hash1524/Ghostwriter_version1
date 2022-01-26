"""This contains all of the URL mappings used by the Users application."""

# Django Imports
from django.urls import path

# Ghostwriter Libraries
from ghostwriter.users.views import user_detail_view, user_redirect_view, user_update_view

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path(
        "profile/update/<int:pk>", user_update_view, name="user_update"
    ),
]
