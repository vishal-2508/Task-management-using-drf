from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login_page/', login_page, name='login_page'),
    path('registration/', RegistrationView.as_view(), name='register'),
    path('registration_page/', registration_page, name='registration_page'),
    # path('registration/', RegistrationView.as_view(), name='register'),
    # path('', include('accounts.urls')),
    # path('task/', include('task.urls')),

]