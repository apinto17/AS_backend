from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import json
from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED
)
from api.serializers.UserSerializer import UserSerializer

# TODO add validator in UserSerializer

class SignUpAPI(generics.GenericAPIView):

    def post(self,request, *args, **kwargs):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            user = serialized.create(request.data)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},
                    status=HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
            
        