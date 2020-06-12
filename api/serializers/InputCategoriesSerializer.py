from rest_framework import serializers

from api.models import Categories


class InputCategoriesSerializer(serializers.Serializer):

    input_category = serializers.CharField(max_length=256)

