from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'full_name', 'first_name',
            'last_name', 'patronymic', 'department'
        )
