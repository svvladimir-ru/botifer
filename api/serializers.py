from rest_framework import serializers
# from users.models import Profile, User
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email',)
        model = User
