from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Assembly


class AssemblySerializer(serializers.ModelSerializer):

    items = serializers.JSONField()
    user_id = serializers.CharField()

    class Meta:
        model = Assembly
        fields = ('id', 'user_id', 'project_name', 'items', 'txntime')
