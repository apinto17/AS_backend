from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('__all__')

