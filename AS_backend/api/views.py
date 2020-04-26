
from .serializers import UserSerializer, CrawledDataSerializer, CategoriesSerializer, ProjectsSerializer
from .models import CrawledData, Projects
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


@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def sign_up(request):
    body = json.loads(request.body)
    username = body['username']
    password = body['password']
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = User(username, password)
    serializer = UserSerializer(user)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    body = json.loads(request.body)
    username = body['username']
    password = body['password']
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)



@csrf_exempt
@api_view(["GET"])
@permission_classes([AllowAny])
def get_item_by_category(request):
    body = json.loads(request.body)
    cat = body['category']
    item_set = CrawledData.objects.filter(input_category=str(cat))
    serializer = CrawledDataSerializer(results_set, many=True)
    return Response(serializer.data)



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


