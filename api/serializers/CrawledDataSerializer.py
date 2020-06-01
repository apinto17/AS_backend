from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import CrawledData


class CrawledDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawledData
        fields = ('__all__')

