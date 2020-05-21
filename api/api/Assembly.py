from api.models import Assembly
from api.serializers.AssemblySerializer import AssemblySerializer
from rest_framework import generics


class AssemblyList(generics.ListCreateAPIView):
    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer


class AssemblyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer