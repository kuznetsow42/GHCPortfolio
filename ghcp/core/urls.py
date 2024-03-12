from django.urls import include, path
from .views import BasicsListView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("basics/", BasicsListView.as_view()),
    path("projects/", include("projects.urls")),
    path("chat/", include("chat.urls")),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
