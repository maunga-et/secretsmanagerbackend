from django.contrib import admin
from .models import Secret, SecretRecord, APIKey

admin.site.register(Secret)
admin.site.register(SecretRecord)
admin.site.register(APIKey)

