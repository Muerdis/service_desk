from django.conf.urls import url, include
from rest_framework import routers

from request.views import RequestReasonViewSet, RequestViewSet, \
    RequestTypeViewSet

router = routers.DefaultRouter()
router.register(r'request-reasons', RequestReasonViewSet, base_name='request-reasons')
router.register(r'requests', RequestViewSet, base_name='requests')
router.register(r'request-types', RequestTypeViewSet, base_name='request-types')

urlpatterns = []

urlpatterns += [
    url(r'^', include(router.urls)),
]