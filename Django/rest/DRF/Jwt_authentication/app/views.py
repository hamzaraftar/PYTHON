from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer ,LoginSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView


# Create your views here.
class RegisterView (generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class LoginView (generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serialized = UserSerializer(user)
            return Response({
                'user': user_serialized.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({
            'message': 'Invalid credentials'
        })

class Dashbord(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        user_serialized = UserSerializer(user)
        return Response({
            'message':"Welcome to Dashbord",
            'user':user_serialized.data
        })
    
