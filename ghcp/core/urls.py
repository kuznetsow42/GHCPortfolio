from django.urls import include, path
from .views import BasicsListView


urlpatterns = [
    path("basics/", BasicsListView.as_view()),
    path("projects/", include("projects.urls")),
    path("chat/", include("chat.urls"))
]
