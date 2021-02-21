from rest_framework import viewsets

from .models import SiteData, Work
from .serializers import SiteDataSerializer, WorkSerializer


class SiteDataViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'category'
    queryset = SiteData.objects.all()
    serializer_class = SiteDataSerializer


class WorkDataViewSet(viewsets.ModelViewSet):
    lookup_field = 'category'
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
