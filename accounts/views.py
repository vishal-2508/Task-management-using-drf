from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializers
# Create your views here.

def login_page(request):
    print("this is login page...")
    return render(request, 'accounts/login.html')

def registration_page(request):
    print("this is registration page...")
    return render(request, 'accounts/registration.html')

class RegistrationView(APIView):
    print('in register : ')
    def post(self, request):
        print('request.data ,........', type(request.data))
        print('request.data ,........', request.data)
        serializer = UserSerializers(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer_class = UserSerializers()
            serializer_class.create_user(request.data)
            # return Response(serialize.data, status=201)
            return Response({
              "message": "User registered successfully"
            }, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=500)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


