from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password", "id"]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = self.Meta.model(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
