from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from service_desk import api_urls

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
    path('auth/obtain_token/', obtain_jwt_token),
    path('auth/refresh_token/', refresh_jwt_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
