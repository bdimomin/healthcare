from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from patient.forms import UserLoginForm
from django.contrib.auth.decorators import login_required
# from doctor.models import Doctor
from appointment.models import Appointment
from users.models import Departments, User, DoctorProfile

@login_required
def homepage(request):
    return render(request,'admin_dashboard/dashboard.html')
    
    
def login_view(request):
    
    # if request.user.is_authenticated: 
    #     return redirect('dashboard') 
    
    
    form= UserLoginForm()
    context={'form':form}
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            if user is not None and request.user.is_superuser:
                login(request,user)
                return redirect('homepage')
            else:
                form=UserLoginForm()
                return render(request,'registration/login.html',context)
    return render(request,'registration/login.html',context)


@login_required(login_url='patient/login/')
def date_doc_appointment(request):
    
   
    doctors=User.objects.filter(role="DOCTOR")
    context={}

    if request.method == 'POST':
        doc_name= request.POST.get('doctor_id')
        date= request.POST.get('date')
        
        appointments=Appointment.objects.filter(doctor_name_id=doc_name, appoinment_date=date).order_by('serial_number')
        
        context={
            'appointments':appointments,
            'doctors':doctors,
        }
        return render(request,'admin_dashboard/datedocwiseapp.html',context)
    
    return render(request,'admin_dashboard/datedocwiseapp.html',{'doctors':doctors})
    
    
    
def doctor_list(request):
    # doctors= User.objects.filter(role="DOCTOR")
    doctors= DoctorProfile.objects.select_related('user').all()
    
    return render(request,'admin_dashboard/doctor_list.html',{'doctors':doctors})


def edit_doctor(request,pk):
    doctor= User.objects.get(pk=pk)
    if request.method == 'POST':
       is_active=request.POST.get('doctor_status')
       doctor= User.objects.get(pk=pk)
       doctor.is_active=is_active
       doctor.save()
       return redirect('listDoctor')
    return render(request,'admin_dashboard/doctor_edit.html',{'doctor':doctor})



def departments(request):
    departments = Departments.objects.all()
    context ={
        'departments': departments
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        departments =Departments.objects.create(name=name).save()
        return render(request,'admin_dashboard/departments.html',context)
        
    return render(request,'admin_dashboard/departments.html',context)