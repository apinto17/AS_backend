
from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Projects


class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = ('user_id', 'project_name', 'items', 'txntime')

        