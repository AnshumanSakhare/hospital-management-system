from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib import messages
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

# Create your views here.
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