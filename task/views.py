from django.shortcuts import render
from .models import *
from .serializers import *
# from rest_framework.authentication import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication   
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status
# Create your views here.

def dashboard_page(request):
    print("this is login page...")
    return render(request, 'task/dashboard.html')

def update_page(request, project_id):
    print("this is update page...")
    return render(request, 'task/update_project.html',{'project_id':project_id})

class ProjectView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        ## pk is None requied.
        # print('project viewss get method ..')
        if pk is not None:
            return Response({'massage':'project id is not requied for get all project detail.'})
        user_object = request.user
        # print(user_object)
        project_detail = Project.objects.filter(user=user_object)
        serializer = ProjectSerializer(project_detail, many=True)
        # return Response(project_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, pk=None):
        if pk is not None:
            return Response({'massage':'project id is not requied for new project create.'})
        serialize = ProjectSerializer(data=request.data, context={'request': request})
        if serialize.is_valid():
            serialize.save(user=request.user)
            # print(serialize.data)
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
            # print(serialize.data)
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is None:
            return Response({'massage':'project id is compulsory requied.'})
        # print('val ::', pk)
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
        # print('request.data ,........', request.data)
        serialize = ManagerTaskSerializer(data=request.data)
        if serialize.is_valid():
            # print('is dome')
            serialize.save()
            # print(serialize.data)
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



# class DashboardView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         pass
    
#     def post(self, request):
#         pass