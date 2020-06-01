from api.models import Categories, CrawledData
from api.serializers.CategoriesSerializer import CategoriesSerializer
from api.serializers.CrawledDataSerializer import CrawledDataSerializer
from api.serializers.CategoriesCrawledDataSerializer import CategoriesCrawledDataSerializer
from rest_framework import generics
from api.pagination import SmallPagesPagination
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response


class CategoryAPI(generics.GenericAPIView):
    
    def get(self,request, *args, **kwargs):
        cat_string = request.data["cat_string"]
        level = request.data["level"]
        categories = None
        if(level == 0):
            categories = Categories.objects.filter(output_category_ui__startswith=cat_string)
        else:
            categories = Categories.objects.filter(output_category_ui__contains=cat_string)
        # TODO find a way to return items
        categories_serializer = CategoriesSerializer(categories, many=True, fields={"level" : level})
        resp = []
        for obj in categories_serializer.data:
            if(obj is not None):
                resp.append(obj)
        return Response(resp, status=HTTP_200_OK)



