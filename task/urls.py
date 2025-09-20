from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard_page/', dashboard_page, name='dashboard_page'),
    path('project/', ProjectView.as_view(), name='project'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_with_id'),
    path('update_project/<int:project_id>/', update_page, name='update_project'),
    path('managertask/', ManagerTaskView.as_view(), name='managertask'),
    path('managertask/<int:pk>/', ManagerTaskView.as_view(), name='managertask_with_id'),
    path('employeetask/', EmployeeTaskView.as_view(), name='employeetask'),
    path('employeetask/<int:pk>/', EmployeeTaskView.as_view(), name='employeetask_with_id'),
    path('massage/', MassageView.as_view(), name='massage'),
    path('massage/<int:pk>/', MassageView.as_view(), name='massage_with_id'),

]