from api.models import CrawledData
from api.serializers.CrawledDataSerializer import CrawledDataSerializer
from rest_framework import generics


class CrawledDataDetail(generics.RetrieveAPIView):
    queryset = CrawledData.objects.all()
    serializer_class = CrawledDataSerializer
