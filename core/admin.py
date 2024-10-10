from django.contrib import admin

# Register your models here.
from .models import Alumni, Student

admin.site.register(Alumni)
admin.site.register(Student)
