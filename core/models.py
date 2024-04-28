from django.db import models
from django.contrib.auth.models import User


class Secret(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class SecretRecord(models.Model):
    secret = models.ForeignKey(Secret, on_delete=models.CASCADE)
    key = models.CharField(max_length=255, blank=False, null=False)
    value = models.CharField(max_length=255, blank=False, null=True)

    def __str__(self):
        return self.secret.user.username
