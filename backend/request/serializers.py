from rest_framework import serializers

from request.models import RequestReason, Request, RequestType


class RequestReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestReason
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    created_user_name = serializers.CharField(source='created_user.get_full_name', read_only=True)
    assigned_user_name = serializers.CharField(source='assigned_user.get_full_name', read_only=True)
    reason_name = serializers.CharField(source='request_reason.text', read_only=True)
    reason_type_name = serializers.CharField(source='request_reason.request_type.name', read_only=True)
    date_created = serializers.DateTimeField(format='%d-%m-%Y %H:%M', read_only=True)
    device_templates_names = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_device_templates_names(instance):
        names = instance.device_templates.values_list('name', flat=True)
        return names

    class Meta:
        model = Request
        fields = (
            'id', 'title', 'text', 'date_created', 'status', 'request_reason', 'reason_type_name', 'reason_name',
            'assigned_user', 'created_user', 'created_user_name',
            'assigned_user_name', 'device_templates', 'device_templates_names'
        )


class RequestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestType
        fields = '__all__'