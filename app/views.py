from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from .models import User, Student
# # Create your views here
from .serializers import UserSerializer, StudentSerializer


class UserList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class StudentList(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
