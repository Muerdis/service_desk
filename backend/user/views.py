from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserSerializer


class UserView(APIView):
    """API для получения информации о пользователе"""

    @staticmethod
    def get(request, *args, **kwargs):
        # user = request.user

        user = User.objects.first() # пока нет авторизации
        serializer = UserSerializer(user)

        return Response(serializer.data)