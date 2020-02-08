from rest_framework import serializers

from .models import Item, User, Assembly


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('description', 'price', 'link', 'category', 'site_name', 'image', 'specs', 'unit', 'time')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name',)



class AssemblySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'items', 'user')

        