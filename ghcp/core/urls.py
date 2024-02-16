from django.urls import path
from .views import BasicsListView


urlpatterns = [
    path("basics/", BasicsListView.as_view())
]
