from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from .serializers import UserSerializer


class CreateUserAPIView(CreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer


class DeleteUserAPIView(DestroyAPIView):
    serializer_class = UserSerializer


class UpdateUserAPIView(UpdateAPIView):
    serializer_class = UserSerializer


class GetUserAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
