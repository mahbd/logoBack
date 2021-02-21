from collections import OrderedDict

from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .models import SiteData, Work
from .serializers import SiteDataSerializer, WorkSerializer


class SiteDataViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'category'
    queryset = SiteData.objects.all()
    serializer_class = SiteDataSerializer


class Pagination12(LimitOffsetPagination):
    default_limit = 12

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.count),
            ('page', self.offset // self.limit + 1),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class WorkDataViewSet(viewsets.ModelViewSet):
    pagination_class = Pagination12
    lookup_field = 'category'
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
