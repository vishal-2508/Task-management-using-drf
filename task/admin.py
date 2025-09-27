from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'attendance_detail', 'user']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'project_start_date', 'project_end_date', 'user']

@admin.register(ManagerTask)
class ManagerTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_name', 'manager_start_date', 'manager_end_date', 'assign', 'project']

@admin.register(EmployeeTask)
class EmployeeTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_start_date', 'employee_end_date', 'user', 'manager_task']

@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ['id', 'massage_detail', 'employee_task']


