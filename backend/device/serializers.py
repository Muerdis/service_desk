from rest_framework import serializers

from device.models import DeviceTemplate


class DeviceTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceTemplate
        fields = '__all__'
