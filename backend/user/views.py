from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer


class UserView(APIView):
    """API для получения информации о пользователе"""

    @staticmethod
    def get(request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)

        return Response(serializer.data)