from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)

from user.views import (
    CreateUserView,
    ManageUserView
)

urlpatterns = [
    path("me/", ManageUserView.as_view(), name="manage"),
    path("register/", CreateUserView.as_view(), name="create"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenObtainPairView.as_view(), name="token_verify"),
]

app_name = "user"
