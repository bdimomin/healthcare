from django.shortcuts import render,redirect
from django.http import HttpResponse
# from doctor.forms import DoctorRegistrationForm,DoctorLoginForm,DoctorProfileUpdate, DoctorProfileDetails
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from doctor.models import Doctor, DoctorsProfile, Departments
from appointment.models import Appointment
from datetime import date
from users.models import User,DoctorProfile
from doctor.forms import DoctorEducationalQualificationsForm,DoctorProfileUpdate
from doctor.models import DoctorEducationalQualifications


@login_required(login_url='/users/login/')
def doctor_home(request):
    return render(request,'doctor/dashboard.html')

# def doctor_reg(request):
#     form = DoctorRegistrationForm()
#     if request.method =='POST':
#         form = DoctorRegistrationForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Congratulations Sir, You have successfully registered. Please Wait for the internal Verification.")
#         else:
#             return HttpResponse("Something Wrong Sir, Please try again")
        
#     return render(request,'doctor/registration.html',{'form':form})


# def doctor_login(request):
#     form = DoctorLoginForm()
#     if request.method == 'POST':
        
#         form = DoctorLoginForm(request.POST)
        
#         if form.is_valid():
#             email=request.POST['email']
#             password=request.POST['password']
#             doctor=authenticate(request,email=email,password=password)
#             if doctor is not None:
#                 login(request,doctor)
#                 return redirect('doctor_home')
                
#             else:
               
#                 form=DoctorLoginForm()
#                 return render(request,'registration/login.html',{'form':form})
            
#     return render(request,'doctor/login.html',{'form':form})

@login_required(login_url='/users/login/')
def doctor_profile_update(request,pk):
    
    try:
        doctor = DoctorProfile.objects.get(user_id=pk)
        form =DoctorProfileUpdate(instance=doctor)
    except:
        form =DoctorProfileUpdate()
    if request.method == 'POST':
        try:
            form=DoctorProfileUpdate(request.POST, request.FILES, instance=doctor)
        except:
            form=DoctorProfileUpdate(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('doctor_home')
    return render(request,'doctor/edit_doctor.html',{'form':form})

@login_required(login_url='/users/login/')
def appointment_list_view(request,pk):
    if request.method=='POST':
        pk = request.user.id
        date = request.POST.get('date')
        appointments = Appointment.objects.filter(doctor_name_id = pk, appoinment_date = date)
        return render(request,'doctor/appointment_list.html', {'appointments': appointments})
    else:
        return render(request,'doctor/appointment_list.html')
    


def doctor_logout(request):
    logout(request)
    return redirect('frontpage')


def profile_doc(request,pk):
    doctor= User.objects.get(pk=pk)
    doctor_details = DoctorProfile.objects.get(user_id=doctor.id)
    details = DoctorEducationalQualifications.objects.filter(doctor_id=pk)
    
    context={
        'doctor':doctor,
        'details':details,
        'doctor_details':doctor_details
    }
    return render(request,'doctor/profile.html',context)

@login_required(login_url='/users/login/')
def doctor_profile_details(request):
    details = DoctorEducationalQualifications.objects.filter(doctor_id=request.user.id)
    if request.method =='POST':
        form = DoctorEducationalQualificationsForm(request.POST)
        form.instance.doctor_id = request.user
        if form.is_valid():
            form.save()
            return redirect('Profile_details')
    else:
        form = DoctorEducationalQualificationsForm()
    return render(request, 'doctor/doctor_profile_details.html',{'form':form,'details':details})
