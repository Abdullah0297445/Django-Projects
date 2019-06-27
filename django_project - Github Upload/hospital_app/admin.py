from django.contrib import admin
from .models import Patient, DiagReport

# Register your models here.
admin.site.register(Patient)
admin.site.register(DiagReport)