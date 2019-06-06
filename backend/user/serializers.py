from rest_framework import serializers

from user.models import User, Department


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователей"""

    full_name = serializers.CharField(source='get_full_name', read_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'id', 'username', 'full_name', 'first_name', 'last_name',
            'middle_name', 'department', 'email', 'password', 'password2'
        )

    def validate(self, attrs):
        data = super(UserSerializer, self).validate(attrs)
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли не совпадают')

        del data['password2']

        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, user, validated_data):
        user.name = validated_data['name']
        user.set_password(validated_data['password'])
        user.save()

        return user


class DepartmentSerializer(serializers.ModelSerializer):
    """Сериализатор для отделов"""

    class Meta:
        model = Department
        fields = '__all__'
