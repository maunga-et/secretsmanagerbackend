from .models import Secret, SecretRecord
from .serializers import SecretSerializer, SecretRecordSerializer
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    ListAPIView
)


class CreateSecretAPIView(CreateAPIView):
    serializer_class = SecretSerializer


class DeleteSecretAPIView(DestroyAPIView):
    serializer_class = SecretSerializer
    queryset = Secret.objects.all()


class UpdateSecretAPIView(UpdateAPIView):
    serializer_class = SecretSerializer
    queryset = Secret.objects.all()


class GetSecretAPIView(RetrieveAPIView):
    serializer_class = SecretSerializer
    queryset = Secret.objects.all()


class ListSecretsAPIView(ListAPIView):
    serializer_class = SecretSerializer

    def get_queryset(self):
        return Secret.objects.filter(user_id=self.kwargs['user_id'])


class CreateSecretRecordAPIView(CreateAPIView):
    serializer_class = SecretRecordSerializer


class DeleteSecretRecordAPIView(DestroyAPIView):
    serializer_class = SecretRecordSerializer
    queryset = SecretRecord.objects.all()


class UpdateSecretRecordAPIView(UpdateAPIView):
    serializer_class = SecretRecordSerializer
    queryset = SecretRecord.objects.all()


class GetSecretRecordAPIView(RetrieveAPIView):
    serializer_class = SecretRecordSerializer
    queryset = SecretRecord.objects.all()


class ListSecretRecordsAPIView(ListAPIView):
    serializer_class = SecretRecordSerializer

    def get_queryset(self):
        return SecretRecord.objects.filter(secret_id=self.kwargs['secret_id'])
