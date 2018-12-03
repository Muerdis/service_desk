from rest_framework import viewsets

from device.models import DeviceTemplate
from device.serializers import DeviceTemplateSerializer


class DeviceTemplateViewSet(viewsets.ModelViewSet):
    """API для шаблонов оборудования"""

    queryset = DeviceTemplate.objects.all().order_by('id')
    serializer_class = DeviceTemplateSerializer
