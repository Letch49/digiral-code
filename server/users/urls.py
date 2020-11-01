from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.api import RegistrationAPI, UserAPI

urlpatterns = [
    path('registration/', RegistrationAPI.as_view(), name='registration'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("me/", UserAPI.as_view(), name='user'),
]
