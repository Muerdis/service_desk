from rest_framework import serializers

from request.models import RequestReason


class RequestReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestReason
        fields = '__all__'