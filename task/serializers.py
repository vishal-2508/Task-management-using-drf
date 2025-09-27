from rest_framework import serializers
from accounts.models import User
from .models import *

class MassageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Massage
        fields = "__all__"

class EmployeeTaskSerializer(serializers.ModelSerializer):
    employeetask_massage = MassageSerializers(read_only=True)

    class Meta:
        model = EmployeeTask
        fields = "__all__"
        include = ["employeetask_massage"]

class ManagerTaskSerializer(serializers.ModelSerializer):
    managertask_employeetask = EmployeeTaskSerializer(read_only=True)

    class Meta:
        model = ManagerTask
        fields = "__all__"
        include = ["managertask_employeetask"]

class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    project_managertask = ManagerTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"
        include = ["project_managertask"]



class ProjectSerializerGetTask(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = "__all__"

class ManagerTaskSerializerGetTask(serializers.ModelSerializer):
    project = ProjectSerializerGetTask(read_only=True)

    class Meta:
        model = ManagerTask
        fields = "__all__"
        include = ["project"]

class EmployeeTaskSerializerGetTask(serializers.ModelSerializer):
    manager_task = ManagerTaskSerializerGetTask(read_only=True)

    class Meta:
        model = EmployeeTask
        fields = "__all__"
        include = ["manager_task"]

class MassageSerializersGetTask(serializers.ModelSerializer):
    employee_task = EmployeeTaskSerializerGetTask(read_only=True)

    class Meta:
        model = Massage
        fields = "__all__"
        include = ["employee_task"]


### this is brother serializer (ProjectSerializer1) after complite the project you can delete this serializers.....

class ProjectSerializer1(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Project
        fields = "__all__"

class ManagerTaskProjectSerializer(serializers.ModelSerializer):
    project = ProjectSerializer1(read_only = True )

    class Meta:
        model = ManagerTask
        # fields = "__all__"
        fields = ["id", "task_name", "manager_start_date","manager_end_date", 'project' ]





class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type'] 





