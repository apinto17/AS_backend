from rest_framework import serializers
from django.contrib.auth.models import User

from .models import CrawledData, Categories, Projects


class CrawledDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrawledData
        fields = ('item_description', 'price', 'item_specifications', 'input_category', 'unit', 'url', 'site_name', 'image_source', 'txntime')


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



class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('primary_category', 'site_name', 'input_category', 'output_category', 'output_category_ui')



class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = ('user_id', 'project_name', 'items', 'txntime')

        