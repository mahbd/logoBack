from rest_framework import serializers

from .models import SiteData, Work


class SiteDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteData
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'
