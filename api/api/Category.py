from api.models import Categories, CrawledData
from api.serializers.CategoriesSerializer import CategoriesSerializer
from api.serializers.CrawledDataSerializer import CrawledDataSerializer
from api.serializers.InputCategoriesSerializer import InputCategoriesSerializer
from rest_framework import generics
from api.pagination import SmallPagesPagination
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from api.views import get_item_filters


class CategoryAPI(generics.GenericAPIView):
    
    def get(self,request, *args, **kwargs):

        ### GET CATEGORIES ##
        # get categories that start with "cat_string" and remove duplicats
        category_string = self.request.GET.get("cat_string")
        categories = Categories.objects.filter(output_category_ui__startswith=category_string + "|").exclude(output_category=None)
        output_category_set = set(categories.values_list("output_category_ui"))
        cat_list = [category[0] for category in output_category_set]
        
        # get sub-categories that are directly below the cat_string in each category in cat_list
        level = category_string.count("|")
        sub_cats = self.get_sub_cats(level, cat_list)

        ### GET ITEMS ##
        # Get all input categories that match "cat_string"
        input_categories = Categories.objects.filter(output_category_ui=category_string).values("input_category")
        input_category_list = [category["input_category"] for category in input_categories]
        
        # Grab all the items from the relevant input categories.
        items = CrawledData.objects.filter(input_category__in=input_category_list)  
        item_serializer = CrawledDataSerializer(items, many=True)
        items = item_serializer.data

        ### GET FILTERS ###
        item_ids = [item["id"] for item in items]
        filters = get_item_filters(item_ids)

        # Throw it all together, and done.
        data = {
            "categories": sub_cats,
            "items": items,
            "filters": filters
        }
        return Response(data, status=HTTP_200_OK)



    def get_sub_cats(self, level, cat_list):
        sub_cats = []
        for cat in cat_list:
            sub_cat = ""
            start = self.find_nth(cat, "|", level + 1) + 1
            end = self.find_nth(cat, "|", level + 2) + 1
            if(end == 0 or end == -1):
                sub_cat = cat[start:]
            else:
                sub_cat = cat[start:end]

            sub_cat = sub_cat.replace("|", "")
            if(sub_cat not in sub_cats and sub_cat != cat):
                sub_cats.append(sub_cat)

        sub_cats.sort()
        return sub_cats



    def find_nth(self, haystack, needle, n):
        if(n == 0):
            return 0
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+len(needle))
            n -= 1
        return start



