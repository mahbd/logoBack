from rest_framework import viewsets

from .models import SiteData
from .serializers import SiteDataSerializer


class SiteDataViewSet(viewsets.ModelViewSet):
    lookup_field = 'category'
    queryset = SiteData.objects.all()
    serializer_class = SiteDataSerializer
