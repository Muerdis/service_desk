from django.conf.urls import url, include
from rest_framework import routers

from request.views import RequestReasonViewset

router = routers.DefaultRouter()
router.register(r'request-reasons', RequestReasonViewset, base_name='request-reasons')

urlpatterns = []

urlpatterns += [
    url(r'^', include(router.urls)),
]