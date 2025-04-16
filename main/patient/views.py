from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Patient, Appointment
from django.db import IntegrityError


def password_reset(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_reset.html', {'form': form})

def home(request):
    return render(request,'home.html')

def login_choice(request):
    return render(request, 'login_choice.html')

def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('patient_dashboard_with_appointment')  # Redirect to new page
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'patient_login.html')

def doctor_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    return render(request, 'doctor_login.html')

def doctor_resetpassword(request):
    return render(request,'doctor_resetpassword.html')

def doctor_logout(request):
    logout(request)
    return redirect('/')

def quick_add_patient(request):
    if request.method == 'POST':
        try:
            from datetime import timedelta
            from django.utils import timezone
            
            # Convert and validate form data
            mobile = request.POST.get('mobile', '').strip()
            if mobile and not mobile.isdigit():
                raise ValueError("Mobile number must contain only digits")
                
            amount = request.POST.get('amount', '0')
            try:
                amount = float(amount)
            except ValueError:
                amount = 0.00
                
            next_visit_days = request.POST.get('nextvisit', '0')
            try:
                next_visit_days = int(next_visit_days)
            except ValueError:
                next_visit_days = 0
                
            patient = Patient(
                name=request.POST.get('name', '').strip(),
                age=int(request.POST.get('age', 0)),
                gender=request.POST.get('gender', 'Male'),
                mobile=mobile,
                address=request.POST.get('address', '').strip(),
                medicine=request.POST.get('medicine', '').strip(),
                detail=request.POST.get('detail', '').strip(),
                note=request.POST.get('note', '').strip(),
                amount=amount,
            )


            patient.save()
            messages.success(request, 'Patient added successfully!')
            return redirect('quick_add_patient')
        except Exception as e:
            messages.error(request, f'Error adding patient: {str(e)}')
    return render(request, 'quick-add-patient-form.html')

def doctor_dashboard(request):
    return render(request,'doctor_dashboard.html')

@login_required
def manage_patients(request):
    patients = Patient.objects.all().order_by('name')
    context = {
        'patients': patients,
        'fields': [
            {'name': 'name', 'label': 'Name'},
            {'name': 'age', 'label': 'Age'},
            {'name': 'gender', 'label': 'Gender'},
            {'name': 'mobile', 'label': 'Mobile'},
            {'name': 'address', 'label': 'Address'},
            {'name': 'medicine', 'label': 'Medicine'},
            {'name': 'detail', 'label': 'Details'},
            {'name': 'note', 'label': 'Notes'},
            {'name': 'amount', 'label': 'Amount'}
        ]

    }
    return render(request, 'manage-patients.html', context)

@login_required
def patient_registration(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, "Passwords don't match")
            return redirect('patient_registration')
            
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Registration successful! Please login.')
            return redirect('patient_login')
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return redirect('patient_registration')
    
    return render(request, 'patient_registration.html')

def delete_patient(request, patient_id):

    try:
        patient = Patient.objects.get(id=patient_id)
        patient.delete()
        messages.success(request, 'Patient deleted successfully!')
    except Patient.DoesNotExist:
        messages.error(request, 'Patient not found!')
    return redirect('manage_patients')

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def patient_dashboard_with_appointment(request):
    return render(request, 'patient_dashboard_with_appointment.html')

def book_appointment(request):
    if request.method == 'POST':
        # Check if the user already has an appointment
        if Appointment.objects.filter(patient_name=request.user.username).exists():
            messages.error(request, 'You already have an appointment booked.')
            return redirect('book_appointment')

        try:
            # Save the form data to the database
            appointment = Appointment(
                patient_name=request.user.username,
                age=request.POST.get('age'),
                gender=request.POST.get('gender'),
                contact=request.POST.get('contact'),
                appointment_date=request.POST.get('appointment_date'),
                doctor_name=request.POST.get('doctor_name'),
                reason=request.POST.get('reason')
            )
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('book_appointment')
        except IntegrityError as e:
            messages.error(request, f'Error booking appointment: {str(e)}')
            return redirect('book_appointment')

    return render(request, 'book_appointment.html')

def view_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'view_appointments.html', {'appointments': appointments})

def new_patient_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful! Please login.')
            return redirect('patient_login')
        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return redirect('new_patient_registration')

    return render(request, 'new_patient_registration.html')

from django.contrib.auth.decorators import login_required

@login_required
def appointment_status(request):
    appointments = Appointment.objects.filter(patient_name=request.user.username)
    return render(request, 'appointment_status.html', {'appointments': appointments})

@login_required
def update_appointment_status(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            appointment.status = 'Confirmed'
            appointment.appointment_time = request.POST.get('appointment_time')
            appointment.additional_details = request.POST.get('additional_details')
            messages.success(request, 'Appointment confirmed successfully!')
        elif 'cancel' in request.POST:
            appointment.status = 'Cancelled'
            appointment.appointment_date = request.POST.get('new_date')
            appointment.appointment_time = request.POST.get('new_time')
            appointment.additional_details = request.POST.get('reschedule_details')
            messages.success(request, 'Appointment rescheduled successfully!')
        appointment.save()
        return redirect('view_appointments')
    return render(request, 'update_appointment_status.html', {'appointment': appointment})

@login_required
def mark_appointment_complete(request, appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id, status='Confirmed')
        appointment.delete()
        messages.success(request, 'Appointment marked as complete and removed successfully!')
    except Appointment.DoesNotExist:
        messages.error(request, 'Appointment not found or not confirmed!')
    return redirect('view_appointments')
