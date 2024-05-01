from rest_framework import status
from rest_framework.response import Response

from .models import Secret, SecretRecord, APIKey
from .serializers import SecretSerializer, SecretRecordSerializer, APIKeySerializer
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    ListAPIView
)


class CreateSecretAPIView(CreateAPIView):
    serializer_class = SecretSerializer

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        name = request.data['name']
        data = {'user': user_id, 'name': name}

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        return Secret.objects.filter(user_id=self.request.user.id)


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


class CreateAPIKeyAPIView(CreateAPIView):
    serializer_class = APIKeySerializer

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        data = {'user': user_id}

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListAPIKeysAPIView(ListAPIView):
    serializer_class = APIKeySerializer

    def get_queryset(self):
        return APIKey.objects.filter(user_id=self.request.user.id)