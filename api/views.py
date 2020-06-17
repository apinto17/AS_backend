
from api.serializers.UserSerializer import UserSerializer 
from api.serializers.CrawledDataSerializer import CrawledDataSerializer
from api.serializers.CategoriesSerializer import CategoriesSerializer
from api.serializers.AssemblySerializer import AssemblySerializer
from .models import CrawledData, Assembly
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.db import connection
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
import requests
import json
from django.contrib.auth.models import User
import datetime



@csrf_exempt
@api_view(["GET"])
@permission_classes([AllowAny])
def item_specs(request):
    item_desc = request.data['item_desc']
    cursor = connection.cursor()

    query = """ SELECT distinct key_name
            ,count(key_name) as count_key
            ,count(key_name) /
            (Select
            count(id) Total_Items
            From AssembledSupply.crawled_data
            where item_description like '%Cutoff%') key_frequency
            FROM AssembledSupply.crawled_data cd,
            JSON_TABLE(JSON_KEYS(cd.item_specifications),
                            '$[*]' COLUMNS (key_name VARCHAR(20) PATH '$')
                            ) AS k
                            where cd.item_description like '%Cutoff%'
                            Group by key_name
                            order by  count(key_name) desc; """

    cursor.execute(query)
    res = cursor.fetchall()
    print(res)

    return Response(status=HTTP_200_OK)




@csrf_exempt
@api_view(["GET"])
@permission_classes([AllowAny])
def search_multiple_items(request):
    useES = request.data['useES']
    search_items = request.data['search_items']
    res = {}
    for search_item in search_items:
        print(search_item)
        results = search_helper(useES, search_item)
        res[search_item] = results

    return Response(res)


def search_helper(useES, search_item):
    if(useES):
        host = 'search-asestest-uuri6jqdjtwsf4siizpeikka2e.us-west-1.es.amazonaws.com' 
        index = 'as-crawled-data'
        wildcard = 'Norton'
        size = '&size=100'
        q = 'q=' + search_item
        url = 'https://' + host + '/' + index + '/_search?' + q + wildcard + size
        r = requests.get(url = url)
        return r.json
    else:
        results_set = CrawledData.objects.filter(item_description__icontains=search_item)
        serializer = CrawledDataSerializer(results_set, many=True)
        return serializer.data


@csrf_exempt
@api_view(["GET"])
@permission_classes([AllowAny])
def search_item(request):
    useES = request.query_params.get('useES')
    search_term = request.query_params.get('search_term')
    if("true" in useES):
        useES = True 
    else:
        useES = False
    
    data = search_helper(useEs, search_term)

    return Response(data)


