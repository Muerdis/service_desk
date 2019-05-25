from rest_framework import serializers

from event.models import Event


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор для мероприятий"""

    class Meta:
        model = Event
        fields = '__all__'
