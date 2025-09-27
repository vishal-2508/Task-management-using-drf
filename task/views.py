from django.shortcuts import render
from accounts.models import User
from .models import *
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication   
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework import generics
# Create your views here.


from accounts.models import User

from rest_framework.generics import RetrieveAPIView
from django.contrib.auth import get_user_model

class UserProfileDetailView(APIView):
    def get(self, request, username):
        ## pk is None requied.
        # if pk is not None:
        #     return Response({'massage':'project id is not requied for get all project detail.'})
        # user_object = request.user
        user_detail = User.objects.filter(username=username, user_type="Employee")
        # print("in user profile ", username)
        # print(user_detail.values())
        # print(user_detail.first())
        serializer = UserProfileSerializer(user_detail, many=True)
        if user_detail.first():
            # print("if condition///")
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"massage":"This User name is not exist."})

# class UserProfileDetailView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserProfileSerializer
#     lookup_field = 'username' # Or 'pk' if looking up by ID

# User = get_user_model()

# class CheckUsernameView(APIView):
#     def get(self, request, *args, **kwargs):
#         username = request.query_params.get('username', None)
#         print("val : ", username)
#         print("val : ", type(username))
#         if username:
#             username_exists = User.objects.filter(username__iexact=username).exists()
#             return Response({'username_exists': username_exists})
#         return Response({'error': 'Username parameter is required'}, status=400)

class TaskDetail(generics.ListAPIView):
    # queryset = EmployeeTask.objects.select_related('manager_task').all()
    # serializer_class = EmployeeSerializer77
    def get(self, request):
        employee_task_queryset = EmployeeTask.objects.all()
        serializer_class = EmployeeTaskSerializerGetTask(employee_task_queryset, many=True)
        # print(serializer_class)
        # print(serializer_class.data)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

def dashboard_page(request):
    print("this is login page...")
    return render(request, 'task/dashboard.html')

def manager_task_page(request, project_id):
    print("this is update page...")
    return render(request, 'task/manager_task.html',{'project_id':project_id})

class ProjectView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        ## pk is None requied.
        if pk is not None:
            return Response({'massage':'project id is not requied for get all project detail.'})
        user_object = request.user
        project_detail = Project.objects.filter(user=user_object)
        serializer = ProjectSerializer(project_detail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, pk=None):
        if pk is not None:
            return Response({'massage':'project id is not requied for new project create.'})
        serialize = ProjectSerializer(data=request.data, context={'request': request})
        if serialize.is_valid():
            serialize.save(user=request.user)
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk is None:
            return Response({'massage':'project id is compulsory requied.'})
        try:
            object = Project.objects.get(id = pk)
        except Exception as e:
            return Response({"massage" : str(e)})
        serialize = ProjectSerializer(object, data=request.data, partial=True, context={'request': request})
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({'massage':'project id is compulsory requied.'})
        try:
            object = Project.objects.get(id = pk)
            object.delete()
            return Response({'success':'delete successfully..'})
        except Exception as e:
            return Response({'massage': str(e)})


class ManagerTaskView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # print('in ManagerTaskView : ')
    def get(self, request, pk=None):
        # print('project viewss get method ..')
        if pk is None:
            return Response({"massage":"please enter project id for getting specific project detail."})
        try:
            project_object = Project.objects.get(id=pk)
        except Exception as e:
            return Response({"massage" : str(e)})
        serializer = ProjectSerializer(instance=project_object)
        # print(serializer)
        # print(type(serializer))
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk=None):
        if pk is not None:
            return Response({'massage':'manager task id is not requied for new manager task create.'})
        print('request.data ,........', request.data)
        serialize = ManagerTaskSerializer(data=request.data)
        if serialize.is_valid():
            # print('is dome')
            serialize.save()
            print(serialize.data)
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        # print('request.data ,........', request.data)
        if pk is None:
            return Response({'massage':'manager task id is compulsory requied.'})
        try:
            object = ManagerTask.objects.get(id = pk)
        except Exception as e:
            return Response({"massage" : str(e)})
        serialize = ManagerTaskSerializer(object, data=request.data)
        if serialize.is_valid():
            serialize.save()
            # print(serialize.data)
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({'massage':'manager task id is compulsory requied.'})
        # print('val ::', pk)
        try:
            object = ManagerTask.objects.get(id = pk)
            object.delete()
            return Response({'success':'delete successfully..'})
        except Exception as e:
            return Response({'massage': str(e)})


class EmployeeTaskView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    print('in EmployeeTaskView : ')
    def get(self, request, pk=None):
        # print('project viewss get method ..')
        if pk is None:
            return Response({"massage":"please enter project id for getting specific project detail."})
        try:
            project_object = Project.objects.get(id=pk)
        except Exception as e:
            return Response({"massage" : str(e)})
        serializer = ProjectSerializer(instance=project_object)
        # print(serializer)
        # print(type(serializer))
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        if pk is not None:
            return Response({'massage':'employee task id is not requied for new employee task create.'})
        # print('request.data ,........', request.data)
        serialize = EmployeeTaskSerializer(data=request.data)
        if serialize.is_valid():
            # print('is dome')
            serialize.save()
            # print(serialize.data)
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
     
    def put(self, request, pk=None):
        # print('request.data ,........', request.data)
        if pk is None:
            return Response({'massage':'employee task id is compulsory requied.'})
        try:
            object = EmployeeTask.objects.get(id = pk)
        except Exception as e:
            return Response({"massage" : str(e)})
        serialize = EmployeeTaskSerializer(object, data=request.data)
        if serialize.is_valid():
            serialize.save()
            # print(serialize.data)
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        if pk is None:
            return Response({'massage':'employee task id is compulsory requied.'})
        # print('val ::', pk)
        try:
            object = EmployeeTask.objects.get(id = pk)
            object.delete()
            return Response({'success':'delete successfully..'})
        except Exception as e:
            return Response({'massage': str(e)})
        

class MassageView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # print('in MassageView : ')
    def get(self, request, pk=None):
        # print('project viewss get method ..')
        if pk is None:
            return Response({"massage":"please enter project id for getting specific project detail."})
        try:
            project_object = Project.objects.get(id=pk)
        except Exception as e:
            return Response({"massage" : str(e)})
        serializer = ProjectSerializer(instance=project_object)
        # print(serializer)
        # print(type(serializer))
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        if pk is not None:
            return Response({'massage':'massage id is not requied for new massage create.'})
        # print('request.data ,........', request.data)
        serialize = MassageSerializers(data=request.data)
        if serialize.is_valid():
            # print('is dome')
            serialize.save()
            # print(serialize.data)
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    ####### this put function is comment in massage .
    def put(self, request, pk=None):
        # print('request.data ,........', request.data)
        if pk is None:
            return Response({'massage':'massage id is compulsory requied.'})
        try:
            object = Massage.objects.get(id = pk)
        except Exception as e:
            return Response({"massage" : str(e)})
        serialize = MassageSerializers(object, data=request.data)
        if serialize.is_valid():
            serialize.save()
            # print(serialize.data)
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({'massage':'massage id is compulsory requied.'})
        # print('val ::', pk)
        try:
            object = Massage.objects.get(id = pk)
            object.delete()
            return Response({'success':'delete successfully..'})
        except Exception as e:
            return Response({'massage': str(e)})

