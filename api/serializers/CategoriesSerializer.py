from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Categories



class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('primary_category', 'site_name', 'input_category', 'output_category', 'output_category_ui')

