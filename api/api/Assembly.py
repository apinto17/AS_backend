from api.models import Assembly
from api.serializers.AssemblySerializer import AssemblySerializer
from rest_framework import generics
import datetime
from rest_framework import status
from rest_framework.response import Response

class AssemblyList(generics.GenericAPIView):
    def post(self, request, format=None):
        request.data["txntime"] = str(datetime.datetime.utcnow())
        serializer = AssemblySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AssemblyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer