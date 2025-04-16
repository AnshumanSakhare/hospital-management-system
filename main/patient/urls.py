from django.urls import path
from . import views


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/choice/', views.login_choice, name='login_choice'),
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('patient/login/', views.patient_login, name='patient_login'),

    path('doctor/resetpassword/', views.doctor_resetpassword, name='doctor_resetpassword'),
    path('doctor/logout/', views.doctor_logout, name='doctor_logout'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor/dashboard/manage-patients/', views.manage_patients, name='manage_patients'),
    path('doctor/dashboard/quick-add-patient/', views.quick_add_patient, name='quick_add_patient'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('doctor/dashboard/manage-patients/delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    path('patient/register/', views.patient_registration, name='patient_registration'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('patient/dashboard/appointment/', views.patient_dashboard_with_appointment, name='patient_dashboard_with_appointment'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('view-appointments/', views.view_appointments, name='view_appointments'),
    path('new-patient-registration/', views.new_patient_registration, name='new_patient_registration'),
    path('appointment-status/', views.appointment_status, name='appointment_status'),
    path('update-appointment-status/<int:appointment_id>/', views.update_appointment_status, name='update_appointment_status'),
    path('mark-appointment-complete/<int:appointment_id>/', views.mark_appointment_complete, name='mark_appointment_complete'),
]
