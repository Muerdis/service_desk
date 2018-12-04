from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserSerializer


class AuthenticatedUserViewSet(APIView):
    """API для получения авторизованного пользователя"""

    @staticmethod
    def get(request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)

        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """API для типов заявки"""

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
