from api.models import Assembly, CrawledData
from api.serializers.AssemblySerializer import AssemblySerializer
from api.serializers.CrawledDataSerializer import CrawledDataSerializer
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

    def get(self, request, *args, **kwargs):
        user_id = self.request.GET.get("user_id")
        projects = Assembly.objects.filter(user_id=user_id)
        serializer = AssemblySerializer(projects, many=True)

        res = []
        projects = serializer.data
        for project in projects:
            item_objects = []
            for item in project["items"]:
                item_objects.append(CrawledData.objects.get(pk=item))
            project["items"] = CrawledDataSerializer(item_objects, many=True).data
            res.append(project)


        return Response(res, status=status.HTTP_200_OK)



class AssemblyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer