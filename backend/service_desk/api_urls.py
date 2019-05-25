from django.conf.urls import url, include
from rest_framework import routers

from device.views import DeviceTemplateViewSet, DeviceViewSet, ReservationViewSet
from event.views import EventViewSet
from news.views import NewsViewSet
from request.views import RequestReasonViewSet, RequestViewSet, \
    RequestTypeViewSet
from user.views import UserViewSet, AuthenticatedUserViewSet, DepartmentViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'departments', DepartmentViewSet, base_name='departments')
router.register(r'request-reasons', RequestReasonViewSet, base_name='request-reasons')
router.register(r'requests', RequestViewSet, base_name='requests')
router.register(r'request-types', RequestTypeViewSet, base_name='request-types')
router.register(r'device-templates', DeviceTemplateViewSet, base_name='device-templates')
router.register(r'devices', DeviceViewSet, base_name='devices')
router.register(r'reservations', ReservationViewSet, base_name='reservations')
router.register(r'news', NewsViewSet, base_name='news')
router.register(r'events', EventViewSet, base_name='events')

urlpatterns = [
    url(
        r'^auth-user',
        AuthenticatedUserViewSet.as_view(),
        name='auth-user'
    ),
]

urlpatterns += [
    url(r'^', include(router.urls)),
]