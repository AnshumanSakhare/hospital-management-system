from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/resetpassword/', views.doctor_resetpassword, name='doctor_resetpassword'),
    path('doctor/logout/', views.doctor_logout, name='doctor_logout'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor/dashboard/manage-patients/', views.manage_patients, name='manage_patients'),
    path('doctor/dashboard/quick-add-patient/', views.quick_add_patient, name='quick_add_patient'),
    path('password_reset/', views.password_reset, name='password_reset'),
]
