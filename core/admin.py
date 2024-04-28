from django.contrib import admin
from .models import Secret, SecretRecord

admin.site.register(Secret)
admin.site.register(SecretRecord)

