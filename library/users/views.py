from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import UserSerializer

from django.shortcuts import render
from django.core.mail import send_mail


class UserViewSet(CreateModelMixin, GenericViewSet):
    """
    ViewSet Class for the creation of the users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetAuthToken(ObtainAuthToken):
    """
    Class to obtain the authentication token
    """
    def post(self, request, *args, **kwargs):
        response = super(GetAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        user_serializer = UserSerializer(user, many=False)
        return Response({'token': token.key, 'user': user_serializer.data})
