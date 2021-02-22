from collections import OrderedDict

from rest_framework import viewsets, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .models import SiteData, Work, NewsletterSubscriber
from .serializers import SiteDataSerializer, WorkSerializer, NewsletterSubscriberSerializer


class SiteDataViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'category'
    queryset = SiteData.objects.all()
    serializer_class = SiteDataSerializer


class Pagination(LimitOffsetPagination):
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
    pagination_class = Pagination
    lookup_field = 'category'
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class NewsletterSubscriberView(generics.CreateAPIView):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer
