from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="verify"),
    path("users/", views.CreateUserAPIView.as_view(), name="create-user"),
    path("users/<int:pk>/delete/", views.DeleteUserAPIView.as_view(), name="delete-user"),
    path("users/<int:pk>/update/", views.UpdateUserAPIView.as_view(), name="update-user"),
    path("users/<int:pk>/", views.GetUserAPIView.as_view(), name="get-user")
]
