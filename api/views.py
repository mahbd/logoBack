from collections import OrderedDict

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import viewsets, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from logo import settings
from .models import SiteData, Work, NewsletterSubscriber, Message
from .serializers import SiteDataSerializer, WorkSerializer, NewsletterSubscriberSerializer, MessageSerializer


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


class MessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


@receiver(post_save, sender=NewsletterSubscriber)
def subscribe_newsletter(sender, instance=None, created=False, **kwargs):
    if created:
        send_mail(subject='Subscribed successfully',
                  message='Thanks for subscribing newsletter. We will send you important event information.',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[instance.email],
                  fail_silently=False)
    else:
        send_mail(subject='Email changed successfully',
                  message='Thanks for subscribing newsletter. We will send you important event information.',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[instance.email],
                  fail_silently=False)
