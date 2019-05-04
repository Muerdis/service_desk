import datetime

from django.db.models import Q
from rest_framework import viewsets

from request.models import RequestReason, Request, RequestType
from request.serializers import RequestReasonSerializer, RequestSerializer, \
    RequestTypeSerializer


class RequestReasonViewSet(viewsets.ModelViewSet):
    """API для причин заявки"""

    queryset = RequestReason.objects.all().order_by('id')
    serializer_class = RequestReasonSerializer

    def get_queryset(self):
        dj_request = self.request
        params = dj_request.query_params

        if params.get('type'):
            req_type = params.get('type')
            return RequestReason.objects.filter(request_type=req_type)

        return RequestReason.objects.all()


class RequestViewSet(viewsets.ModelViewSet):
    """API для заявок"""

    queryset = Request.objects.all().order_by('id')
    serializer_class = RequestSerializer

    def get_queryset(self):
        dj_request = self.request
        params = dj_request.query_params
        queryset = Request.objects.filter(
            Q(assigned_user=dj_request.user) | Q(created_user=dj_request.user)
        )

        if params.get('reason'):
            reason = params.get('reason')
            queryset = queryset.filter(request_reason=reason)

        if params.get('create_date_from'):
            create_date_from = params.get('create_date_from')
            create_date_from = datetime.datetime.strptime(
                create_date_from, '%Y-%m-%d'
            )
            queryset = queryset.filter(date_created__gte=create_date_from)

        if params.get('create_date_to'):
            create_date_to = params.get('create_date_to')
            create_date_to = datetime.datetime.strptime(
                create_date_to, '%Y-%m-%d'
            )
            queryset = queryset.filter(date_created__lte=create_date_to)

        if params.get('assigned_user'):
            assigned_user = params.get('assigned_user')
            queryset = queryset.filter(assigned_user=assigned_user)

        if params.get('created_user'):
            created_user = params.get('created_user')
            queryset = queryset.filter(created_user=created_user)

        if params.get('status'):
            status = params.get('status')
            queryset = queryset.filter(status=status)

        return queryset


class RequestTypeViewSet(viewsets.ModelViewSet):
    """API для типов заявки"""

    queryset = RequestType.objects.all().order_by('id')
    serializer_class = RequestTypeSerializer
