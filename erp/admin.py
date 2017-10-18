from django.contrib import admin
from .models import Department
from .models import Faculty

admin.site.register(Department)
admin.site.register(Faculty)