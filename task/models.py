from django.db import models
from accounts.models import User
from django.db.models import JSONField
# Create your models here.

class Attendance(models.Model):
    attendance_detail = models.JSONField(default=dict)
    user = models.OneToOneField(User, related_name='user_attendance', on_delete=models.CASCADE)

class Project(models.Model):
    project_name = models.CharField(max_length=70)
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    user = models.ForeignKey(User, related_name='user_project', on_delete=models.CASCADE)

class ManagerTask(models.Model):
    task_name = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()
    assign = models.CharField(max_length=50)
    project = models.ForeignKey(Project, related_name='project_managertask', on_delete=models.CASCADE)

class EmployeeTask(models.Model):
    task_start_date = models.DateTimeField(null=True)
    task_end_date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manager_task = models.OneToOneField(ManagerTask, related_name='managertask_employeetask', on_delete=models.CASCADE)

class Massage(models.Model):
    massage_detail = models.JSONField(default=list)
    employee_task = models.OneToOneField(EmployeeTask, related_name='employeetask_massage', on_delete=models.CASCADE)
