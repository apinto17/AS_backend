from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import CrawledData


class CrawledDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CrawledData
        fields = ('item_description', 'price', 'item_specifications', 'input_category', 'unit', 'url', 'site_name', 'image_source', 'txntime')

