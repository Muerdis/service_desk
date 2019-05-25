from rest_framework import viewsets

from event.models import Event
from event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """API для мероприятий"""

    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer
