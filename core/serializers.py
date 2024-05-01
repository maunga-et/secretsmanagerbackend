from rest_framework import serializers
from .models import Secret, SecretRecord, APIKey
import random
import string


class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = "__all__"


class SecretRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretRecord
        fields = "__all__"


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = "__all__"

    def create(self, validated_data):
        api_key = APIKey.objects.create(**validated_data)
        characters = string.ascii_letters + string.digits
        api_key.key = ''.join(random.choice(characters) for _ in range(32))
        api_key.save()
        return api_key
