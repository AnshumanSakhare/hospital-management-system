from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def doctor_login(request):
    return render(request,'doctor_login.html')
def doctor_resetpassword(request):
    return render(request,'doctor_resetpassword.html')