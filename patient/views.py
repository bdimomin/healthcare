from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import PatientRegistrationForm,UserLoginForm,ProfileEditForm
from .models import Patient
from django.contrib import messages
from users.models import User



@login_required(login_url='/users/login/')
def home_view(request):
    return render(request,'patient_dashboard/dashboard.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard') 
    context={}
    if request.method=="POST":
        form=PatientRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
        context['register_form']=form
    else:
        form=PatientRegistrationForm()
        context['register_form']=form
    return render(request,'registration/sign_up.html',context)


# def login_view(request):
#     if request.user.is_authenticated: 
#         return redirect('dashboard') 
    
    
#     form= UserLoginForm()
#     context={'form':form}
#     if request.method=="POST":
#         form=UserLoginForm(request.POST)
#         if form.is_valid():
#             email=request.POST['email']
#             password=request.POST['password']
#             user=authenticate(request,email=email,password=password)
            
#             if user is not None and user.is_admin:
#                 login(request,user)
#                 return redirect('homepage')
            
#             elif user is not None:
#                 if 'next' in request.POST:
#                     login(request,user)
#                     return redirect(request.POST.get('next'))
#                 else:
#                     login(request,user)
#                     return(redirect('dashboard'))
                
#             else:
#                 form=UserLoginForm()
#                 return render(request,'registration/login.html',context)
#     return render(request,'registration/login.html',context)

@login_required(login_url='/users/login/')
def profile_edit(request,pk):
    patient= User.objects.get(pk=pk)
    form =ProfileEditForm(instance=patient)
    if request.method == 'POST':
        form=ProfileEditForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request,'patient_dashboard/edit_patient.html',{'form':form})



def logout_view(request):
    logout(request)
    return redirect('frontpage')
        