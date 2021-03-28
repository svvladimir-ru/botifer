from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import User_path
from .serializers import UserSerializer
from rest_framework.views import APIView


User = get_user_model()


class APIUser(APIView):
    """Передаем имя, емеил, сохраняем визит"""
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        user_path = User_path()
        user_path.username = user.username
        user_path.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)
