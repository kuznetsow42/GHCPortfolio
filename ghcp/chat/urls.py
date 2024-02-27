from django.urls import path
from .views import ChatCreateView, MessageView


urlpatterns = [
    path("create/", ChatCreateView.as_view()),
    path("", MessageView.as_view()),
]
