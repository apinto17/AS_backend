
from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Assembly


class AssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = Assembly
        fields = ('user_id', 'project_name', 'items', 'txntime')

        