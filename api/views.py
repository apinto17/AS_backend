
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
def get_item_by_category(request):
    body = json.loads(request.body)
    cat = body['category']
    item_set = CrawledData.objects.filter(input_category=str(cat))
    serializer = CrawledDataSerializer(results_set, many=True)
    return Response(status=HTTP_200_OK)



@csrf_exempt
@api_view(["GET"])
@permission_classes([AllowAny])
def search_item(request):
    useES = request.query_params.get('useES')
    if("true" in useES):
        useES = True 
    else:
        useES = False
    if(useES):
        host = 'search-asestest-uuri6jqdjtwsf4siizpeikka2e.us-west-1.es.amazonaws.com' 
        index = 'as-crawled-data'
        wildcard = 'Norton'
        size = '&size=100'
        q = 'q='
        url = 'https://' + host + '/' + index + '/_search?' + q + wildcard + size
        r = requests.get(url = url)
        return Response(r.json())
    else:
        results_set = CrawledData.objects.filter(item_description__icontains=request.query_params.get('search_term'))
        serializer = CrawledDataSerializer(results_set, many=True)
        return Response(serializer.data)


