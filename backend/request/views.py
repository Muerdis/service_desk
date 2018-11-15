import datetime

from rest_framework import viewsets

from request.models import RequestReason, Request
from request.serializers import RequestReasonSerializer, RequestSerializer


class RequestReasonViewSet(viewsets.ModelViewSet):
    """API для причин заявки"""

    queryset = RequestReason.objects.all()
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

    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get_queryset(self):
        dj_request = self.request
        params = dj_request.query_params
        queryset = Request.objects.all()

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

        if params.get('owner'):
            owner = params.get('owner')
            queryset = queryset.filter(owner=owner)

        if params.get('status'):
            status = params.get('status')
            queryset = queryset.filter(status=status)

        return queryset