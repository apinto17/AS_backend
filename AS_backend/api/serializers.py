from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Item, Assembly


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('description', 'price', 'link', 'category', 'site_name', 'image', 'specs', 'unit', 'time')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name',)

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(make_password(validated_data['password']))
        user.save()
        return user



class AssemblySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'items', 'user')

        