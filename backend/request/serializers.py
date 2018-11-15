from rest_framework import serializers

from request.models import RequestReason, Request


class RequestReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestReason
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'