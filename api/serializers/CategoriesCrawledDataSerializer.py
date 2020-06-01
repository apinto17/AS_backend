from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Categories
from api.serializers.CategoriesSerializer import CategoriesSerializer
from api.serializers.CrawledDataSerializer import CrawledDataSerializer



class CategoriesCrawledDataSerializer(serializers.Serializer):
    categories = CategoriesSerializer()
    items = CrawledDataSerializer()

