from django.contrib import admin

# Register your models here.
from app.models import User, Student

admin.site.register(User)
admin.site.register(Student)