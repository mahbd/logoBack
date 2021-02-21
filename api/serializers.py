from rest_framework import serializers

from .models import SiteData


class SiteDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteData
        fields = '__all__'
