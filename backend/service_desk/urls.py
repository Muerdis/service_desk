from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from service_desk import api_urls

urlpatterns = [
    path('auth/obtain_token/', obtain_jwt_token),
    path('auth/refresh_token/', refresh_jwt_token),
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
