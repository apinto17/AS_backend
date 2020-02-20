
from .serializers import UserSerializer, ItemSerializer, AssemblySerializer
from .models import Item, Assembly
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
    username = request.headers['username']
    password = request.headers['password']
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
    username = request.headers['username']
    password = request.headers['password']
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
def get_item_by_category(request):
    queryset = Item.objects.filter(category=request.GET["category"])
    serializer = ItemSerializer(queryset, many=True)
    return Response(serializer.data)



@csrf_exempt
@api_view(["GET"])
def search_item(request):
    host = 'search-asestest-uuri6jqdjtwsf4siizpeikka2e.us-west-1.es.amazonaws.com' 
    index = 'as-crawled-data'
    wildcard = 'Norton'
    size = '&size=100'
    q = 'q='
    url = 'https://' + host + '/' + index + '/_search?' + q + wildcard + size
    r = requests.get(url = url)
    return Response(r.json())



