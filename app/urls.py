from django.urls import path
from .import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name="users"),
    path('students/', views.StudentList.as_view(), name="students"),
]