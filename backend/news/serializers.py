from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор для новостей"""

    class Meta:
        model = News
        fields = '__all__'
