from django.urls import path
from . import views

urlpatterns = [
    # Secret endpoints
    path("secret/", views.CreateSecretAPIView.as_view(), name="create-secret"),
    path("secret/<int:pk>/delete/", views.DeleteSecretAPIView.as_view(), name="delete-secret"),
    path("secret/<int:pk>/update/", views.UpdateSecretAPIView.as_view(), name="update-secret"),
    path("secret/<int:user_id>/list/", views.ListSecretsAPIView.as_view(), name="list-secrets"),
    path("secret/<int:pk>/", views.GetSecretAPIView.as_view(), name="get-secret"),

    # Secret records endpoints
    path("secret-record/", views.CreateSecretRecordAPIView.as_view(), name="create-secret-record"),
    path("secret-record/<int:pk>/delete/", views.DeleteSecretRecordAPIView.as_view(), name="delete-secret-record"),
    path("secret-record/<int:pk>/update/", views.UpdateSecretRecordAPIView.as_view(), name="update-secret-record"),
    path("secret-record/<int:secret_id>/list/", views.ListSecretRecordsAPIView.as_view(), name="list-secrets-records"),
    path("secret-record/<int:pk>/", views.GetSecretRecordAPIView.as_view(), name="get-secret-record")
]
