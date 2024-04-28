from rest_framework import serializers
from .models import Secret, SecretRecord


class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secret
        fields = "__all__"


class SecretRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretRecord
        fields = "__all__"
