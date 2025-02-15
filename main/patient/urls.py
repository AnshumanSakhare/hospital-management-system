from django.urls import path
from . import views
from .views import password_reset

urlpatterns=[
    path('',views.home,name='home'),
    path('doctor/login',views.doctor_login,name='doctor_login'),
    path('doctor/logout',views.doctor_logout,name='doctor_logout'),
    path('password-reset/', password_reset, name='password_reset'),
]