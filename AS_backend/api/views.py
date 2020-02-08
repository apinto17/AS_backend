from django.shortcuts import render

from rest_framework import viewsets

from .serializers import UserSerializer, ItemSerializer, AssemblySerializer
from .models import User, Item, Assembly
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer



class ItemViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Item.objects.filter(category=request.query_params.get("category"))
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)
