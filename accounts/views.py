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



# class RegistrationView(APIView):
#     #    = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#     # print('in registration :: ')
#     def post(self, request):
#         print('request.data ,........', type(request.data))
#         print('request.data ,........', request.data)
#         serializer = UserSerializers(data=request.data)
#         print(type(serializer))
#         if serializer.is_valid():
#             serializer.save()
#             print("save : ", serializer.data)
#             # return Response(serialize.data, status=201)
#             return Response({
#               "message": "User registered successfully"
#             }, status=status.HTTP_201_CREATED)
#         # return Response(serializer.errors, status=500)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    # def get(self, request, pk=None):
    #     print('request.user .................. ', request.user)
    #     print('request.data ,......111..', request.data)

    #     # stu_data = Student.objects.get(id = 1)
    #     if pk is not None:
    #         stu_data = Student.objects.filter(id = pk)
    #     else:    
    #         stu_data = Student.objects.all()
    #     serializer = StudentSerializers(stu_data, many=True)
    #     print('serila ;: ' ,serializer.data)

    #     return Response(serializer.data)
    




# from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib.auth import authenticate, login
# from django.contrib import messages
# from .models import User
# from django.contrib.auth import logout

# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user_type = request.POST.get('user_type').capitalize()
#         user_object = User.objects.filter(username=username).first()
#         if user_object != None:
#             if user_type == user_object.user_type:
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     messages.success(request, "login successfully.")
#                     ## this login use for one time login then you can not login again without refersh page.
#                     login(request, user)
#                     return HttpResponseRedirect(reverse('dashboard_page'))
#                 else:
#                     messages.error(request, 'invalid password.')
#             else:
#                     messages.error(request, 'Please select correct User type')                    
#         else:
#             messages.error(request, 'User not exitst.')
#     return render(request, 'accounts/login.html')

# def registration_page(request):
#     if request.method == 'POST':
#         user_type = request.POST.get('user_type').capitalize()
#         if user_type != 'Manager' and user_type != 'Employee' :
#             messages.error(request, 'Please write correct User type')
#             return render(request, 'accounts/registration.html')
#         username = request.POST.get('username')
#         if User.objects.filter(username=username).first() != None:
#             messages.error(request, 'User name already exist.')
#             return render(request, 'accounts/registration.html')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         user = User.objects.create_user(
#             user_type=user_type,
#             username=username,
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#         )
#         user.set_password(password)
#         user.save()
#         messages.success(request, "Account created Successfully!")        
#         return redirect('login_page')
#     return render(request, 'accounts/registration.html')


# def logout_page(request):
#     logout(request)
#     return redirect('login_page')



