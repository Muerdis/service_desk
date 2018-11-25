from rest_framework import serializers

from request.models import RequestReason, Request, RequestType


class RequestReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestReason
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    created_user_name = serializers.CharField(source='created_user.get_full_name', read_only=True)
    reason_name = serializers.CharField(source='request_reason.text', read_only=True)
    reason_type_name = serializers.CharField(source='request_reason.request_type.name', read_only=True)
    date_created = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Request
        fields = (
            'id', 'title', 'text', 'date_created', 'status', 'request_reason', 'reason_type_name',
            'reason_name', 'assigned_user', 'created_user', 'created_user_name'
        )


class RequestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestType
        fields = '__all__'