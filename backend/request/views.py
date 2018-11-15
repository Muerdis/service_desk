from rest_framework import viewsets

from request.models import RequestReason
from request.serializers import RequestReasonSerializer


class RequestReasonViewset(viewsets.ModelViewSet):
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