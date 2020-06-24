from api.models import Categories, CrawledData
from api.serializers.CategoriesSerializer import CategoriesSerializer
from api.serializers.CrawledDataSerializer import CrawledDataSerializer
from api.serializers.CategoriesCrawledDataSerializer import CategoriesCrawledDataSerializer
from api.serializers.InputCategoriesSerializer import InputCategoriesSerializer
from rest_framework import generics
from api.pagination import SmallPagesPagination
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response


class CategoryAPI(generics.GenericAPIView):
    

    def get(self,request, *args, **kwargs):
        # make query
        cat_string = self.request.GET.get("cat_string")
        level = int(self.request.GET.get("current_level"))
        categories = Categories.objects.filter(output_category_ui__startswith=cat_string)
        item_cats = Categories.objects.filter(output_category_ui__exact=cat_string).values("input_category")

        # get corresponding items if they exist
        input_cats_raw = InputCategoriesSerializer(item_cats, many=True)
        input_cats_list_dicts = list(input_cats_raw.data)
        input_cats = list(map(lambda x : x["input_category"], input_cats_list_dicts))
        print(input_cats)
        items = CrawledData.objects.filter(input_category__in=input_cats)  

        # serializer data
        categories_serializer = CategoriesCrawledDataSerializer(categories, many=True, fields={"level" : level})
        items = CrawledDataSerializer(items, many=True)

        # format output
        resp = {}
        cat_list = []
        for obj in categories_serializer.data:
            if(obj is not None):
                cat_list.append(obj)
        resp["categories"] = cat_list
        resp["items"] = items.data
        return Response(resp, status=HTTP_200_OK)
