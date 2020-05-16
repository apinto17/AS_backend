from rest_framework import serializers
from django.contrib.auth import authenticate

from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User(
            username=validated_data['email']
        )
        user.set_password(make_password(validated_data['password']))
        user.save()
        return user

