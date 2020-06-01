from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Categories



class CategoriesSerializer(serializers.Serializer):
    output_category_ui = serializers.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        self.instance_list = []
        if fields is not None:
            self.level = fields["level"]
        else:
            self.level = None
        # Instantiate the superclass normally
        super(CategoriesSerializer, self).__init__(*args, **kwargs) 
        

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if(self.level is not None):
            start = self.find_nth(ret["output_category_ui"], "|", self.level + 1) + 1
            end = self.find_nth(ret["output_category_ui"], "|", self.level + 2)
            if(ret['output_category_ui'][start:end] not in self.instance_list):
                ret['category'] = ret['output_category_ui'][start:end]
                self.instance_list.append(ret['output_category_ui'][start:end])
                # del ret["output_category_ui"]
            else:
                ret = None
        return ret

    def find_nth(self, haystack, needle, n):
        if(n == 0):
            return 0
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+len(needle))
            n -= 1
        return start


