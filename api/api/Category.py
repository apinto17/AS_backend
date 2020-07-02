from api.models import Categories, CrawledData
from api.serializers.CategoriesSerializer import CategoriesSerializer
from api.serializers.CrawledDataSerializer import CrawledDataSerializer
from api.serializers.InputCategoriesSerializer import InputCategoriesSerializer
from rest_framework import generics
from api.pagination import SmallPagesPagination
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response


class CategoryAPI(generics.GenericAPIView):
    
    def get(self,request, *args, **kwargs):
        # Query parameters are typically used for GET requests.
        category_string = self.request.GET.get("cat_string")
        
        # We only want the sub-categories, so we add the | to the end of the category string.
        # This ensures that we don't get similarly named categories that are at the same level as the category string.
        categories = Categories.objects.filter(output_category_ui__startswith=category_string + "|").exclude(output_category=None)
        
        # Lots of categories are duplicated, casting the list to a set fixes this.
        output_category_set = set(categories.values_list("output_category_ui"))
        
        # List comprehension, fast and readable. For each output category, grabs the lowest level and formats the data.
        # category_list = [{"category": category[0].split("|")[-1]} for category in output_category_set]
        cat_list = [category[0] for category in output_category_set]
        print(len(cat_list))
        # # Throw all relevant input categories into a list.
        # input_categories = Categories.objects.filter(output_category_ui=category_string).values("input_category")
        
        # # Extracts the relevant string from each input category.
        # input_category_list = [category["input_category"] for category in input_categories]
        
        # # Grab all the items from the relevant input categories.
        # items = CrawledData.objects.filter(input_category__in=input_category_list)  
        
        # # Serialize the data.
        # item_serializer = CrawledDataSerializer(items, many=True)
        
        # # Throw it all together, and done.
        # data = {
        #     "categories": category_list,
        #     "items": item_serializer.data
        # }
        return Response(status=HTTP_200_OK)
