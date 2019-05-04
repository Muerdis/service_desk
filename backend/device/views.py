from rest_framework import viewsets

from device.models import DeviceTemplate, Device
from device.serializers import DeviceTemplateSerializer, DeviceSerializer


class DeviceTemplateViewSet(viewsets.ModelViewSet):
    """API для шаблонов оборудования"""

    queryset = DeviceTemplate.objects.all().order_by('id')
    serializer_class = DeviceTemplateSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    """API для оборудования"""

    queryset = Device.objects.all().order_by('id')
    serializer_class = DeviceSerializer
