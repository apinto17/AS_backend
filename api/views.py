
from api.serializers.UserSerializer import UserSerializer 
from api.serializers.CrawledDataSerializer import CrawledDataSerializer
from api.serializers.CategoriesSerializer import CategoriesSerializer
from api.serializers.AssemblySerializer import AssemblySerializer
from api.serializers.SpecsSerializer import SpecsSerializer
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
    freq_level = .5
    items = ["249371"]
    cursor = connection.cursor()

    item_params = "("
    for item in items:
        if(not item.isdigit()):
            return Response(status=HTTP_400_BAD_REQUEST)
        item_params += "'" + str(item) + "',"
    item_params = item_params[:-1]
    item_params += ")"


    query = """ Select
            q1.key_name Key_Name
            ,group_concat(Distinct q1.elements)
            ,count(key_name) Key_Name_Count
            ,count(key_name) /
            (Select
            count(id) Total_Items
            From crawled_data
            where id in """ + item_params + """) Key_Frequency
            from
            (
            Select
            k.key_name
            ,json_unquote(Json_extract(cd.item_specifications,concat('$."',k.key_name,'"'))) elements
            FROM crawled_data cd,
            JSON_TABLE(JSON_KEYS(cd.item_specifications),
                            '$[*]' COLUMNS (key_name VARCHAR(20) PATH '$')
                            ) AS k
                            where cd.id in """ + item_params + """
            )q1
            group by q1.key_name
            order by count(q1.key_name) desc """

    cursor.execute(query)
    res = cursor.fetchall()

    serializer = SpecsSerializer(res, freq_level)


    return Response(serializer.data(), status=HTTP_200_OK)




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
    
    data = search_helper(useES, search_term)

    return Response(data)


