from rest_framework import serializers

from request.models import RequestReason, Request, RequestType


class RequestReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestReason
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class RequestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestType
        fields = '__all__'