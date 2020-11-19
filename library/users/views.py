from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets

from .serializers import UserSerializer


# http://www.cdrf.co/3.9/rest_framework.mixins/CreateModelMixin.html
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(GetAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        user_serializer = UserSerializer(user, many=False)
        return Response({'token': token.key, 'user': user_serializer.data})


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)