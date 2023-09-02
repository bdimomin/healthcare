from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Departments
from .forms import PatientForm, DoctorForm, DoctorProfileForm


def doctor_registration(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    return render(request,'users/doctor/sign_up.html',{'form':form})

def login_view(request):
    if request.user.is_authenticated and request.user.role=="PATIENT": 
        return redirect('dashboard')
    
    elif request.user.is_authenticated and request.user.role=="DOCTOR":
        return redirect('doctor_home')
    
    elif request.user.is_authenticated and request.user.role=="ADMIN": 
        return redirect('homepage')

    if request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        
        if user is not None and user.role =="PATIENT":
            
           if 'next' in request.POST:
                login(request,user)
                return redirect(request.POST.get('next'))
           else:
               login(request,user)
               return(redirect('dashboard'))
           
        elif user is not None and user.role=="DOCTOR":
            login(request,user)
            return redirect('doctor_home')
        elif user is not None and user.role=="ADMIN":
            login(request,user)
            return redirect('homepage')
        
            
    return render(request,'users/login.html')


def patient_registration(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    return render(request,'users/patient/sign_up.html',{'form':form})

def doctor_profile_edit(request):
    # return render(request,'doctor/)
    pass



