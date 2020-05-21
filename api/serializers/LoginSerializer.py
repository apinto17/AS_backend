from rest_framework import serializers
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from api.exceptions import LoginException


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return User.objects.get(user=user)
        raise LoginException()


