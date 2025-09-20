from rest_framework import serializers
from .models import *

class MassageSerializers(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    # print('password : ', password)
    class Meta:
        model = Massage
        fields = "__all__"
        # include = "managertask_employeetask"
        # fields = ['massage_detail']

class EmployeeTaskSerializer(serializers.ModelSerializer):
    employeetask_massage = MassageSerializers(read_only=True)

    class Meta:
        model = EmployeeTask
        fields = "__all__"
        include = ["employeetask_massage"]
        # fields = ['task_start_date', 'task_end_date', 'employeetask_massage']

# class EmployeeTaskSerializer(serializers.ModelSerializer):
#     # employeetask_massage = MassageSerializers(many=True, read_only=True)

#     class Meta:
#         model = EmployeeTask
#         fields = ['task_start_date', 'task_end_date']

class ManagerTaskSerializer(serializers.ModelSerializer):
    managertask_employeetask = EmployeeTaskSerializer(read_only=True)

    class Meta:
        model = ManagerTask
        fields = "__all__"
        include = ["managertask_employeetask"]
        # fields = ['task_name', 'start_date', 'end_date', 'assign', 'managertask_employeetask']

class ProjectSerializer(serializers.ModelSerializer):
    project_managertask = ManagerTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
        include = ["project_managertask"]
        # fields = ['project_name', 'project_start_date', 'project_end_date', 'project_managertask']

