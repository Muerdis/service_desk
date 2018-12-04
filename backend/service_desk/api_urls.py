from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from device.views import DeviceTemplateViewSet
from request.views import RequestReasonViewSet, RequestViewSet, \
    RequestTypeViewSet
from user.views import UserView, UserViewSet

router = routers.DefaultRouter()
router.register(r'auth/obtain_token', UserViewSet, obtain_jwt_token)
router.register(r'auth/refresh_token', UserViewSet, refresh_jwt_token)
router.register(r'users', UserViewSet, base_name='users')
router.register(r'request-reasons', RequestReasonViewSet, base_name='request-reasons')
router.register(r'requests', RequestViewSet, base_name='requests')
router.register(r'request-types', RequestTypeViewSet, base_name='request-types')
router.register(r'device-templates', DeviceTemplateViewSet, base_name='device-templates')

urlpatterns = [
    url(
        r'^user-info',
        UserView.as_view(),
        name='user-info'
    ),
]

urlpatterns += [
    url(r'^', include(router.urls)),
]