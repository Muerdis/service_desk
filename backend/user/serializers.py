from rest_framework import serializers

from user.models import User, Department


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователей"""

    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'full_name', 'first_name',
            'last_name', 'middle_name', 'department'
        )


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор для отделов"""

    class Meta:
        model = Department
        fields = '__all__'
