from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

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
