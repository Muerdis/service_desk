from rest_framework import viewsets

from news.models import News
from news.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """API для новостей"""

    queryset = News.objects.all().order_by('id')
    serializer_class = NewsSerializer
