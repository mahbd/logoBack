from rest_framework import serializers

from .models import SiteData, Work, NewsletterSubscriber, Message


class SiteDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteData
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'


class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = '__all__'
