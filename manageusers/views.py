from typing import List
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets,generics
from rest_framework.views import APIView
from .serializers import *
from .models import *
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions
from .serializers import UserSerializer,LoginSerializer
from rest_framework import status
from django_rest_allauth.api.views import LoginUserView as lgview

from rest_framework import generics
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.

# class Logout(APIView):
#     def get(self, request, format=None):
#         # simply delete the token to force a login
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    # authentication_classes = [SessionAuthentication, BasicAuthentication]

class LoginUserView(lgview):
    lookup_field = 'pk'
    serializer_class = LoginSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(): 
            password = serializer.validated_data['password']
            if 'email' in serializer.validated_data and 'username' in serializer.validated_data: #if the email and username is passed, authenticate with both
                email = serializer.validated_data['email']
                username = serializer.validated_data['username']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        user_token = Token.objects.get_or_create(user=user)
                        user_token = user_token[0]
                        user_token = user_token.key
                        userdetails = {}
                        userdetails['username'] = user.username
                        userdetails['email'] = user.email
                        userdetails['token'] = user_token
                        userdetails['first_name'] = user.first_name
                        userdetails['last_name'] = user.last_name
                        return Response(userdetails, status=HTTP_200_OK)
                else:
                    data = {"message":"Invalid Login Details"}
                    return Response(data, status=HTTP_400_BAD_REQUEST)
                
            elif 'email' in serializer.validated_data: #if email is passed, authenticate with email
                email = serializer.validated_data['email']
                theu = email.find('@')
                username = email[:theu]
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        user_token = Token.objects.get_or_create(user=user)
                        user_token = user_token[0]
                        user_token = user_token.key
                        userdetails = {}
                        userdetails['username'] = user.username
                        userdetails['email'] = user.email
                        userdetails['token'] = user_token
                        userdetails['first_name'] = user.first_name
                        userdetails['last_name'] = user.last_name
                        return Response(userdetails, status=HTTP_200_OK)
                else:
                    data = {"message":"Invalid Login Details"}
                    return Response(data, status=HTTP_400_BAD_REQUEST)
            elif 'username' in serializer.validated_data: #if username is passed, authenticate with username
                username = serializer.validated_data['username']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        user_token = Token.objects.get_or_create(user=user)
                        user_token = user_token[0]
                        user_token = user_token.key
                        userdetails = {}
                        userdetails['username'] = user.username
                        userdetails['email'] = user.email
                        userdetails['token'] = user_token
                        userdetails['first_name'] = user.first_name
                        userdetails['last_name'] = user.last_name
                        return Response(userdetails, status=HTTP_200_OK)
                else:
                    data = {"message":"Invalid Login Details"}
                    return Response(data, status=HTTP_400_BAD_REQUEST)
        else:
            data = {"message":serializer.errors}
            return Response(data, status=HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        qs = []
        return qs


# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
#   authentication_classes = (TokenAuthentication,)
#   permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
#   permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class SimpleUserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = SimpleUser.objects.all()
#     serializer_class = SimpleUserSerializer


# class AdminUserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = AdminUser.objects.all()
#     serializer_class = AdminUserSerializer

