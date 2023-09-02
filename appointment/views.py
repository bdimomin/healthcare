from django.shortcuts import render,redirect
# from doctor.models import Doctor, Departments
from appointment.models import Appointment
from patient.models import Patient
# from doctor.models import Doctor

from django.db.models import Max
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from twilio.rest import Client
from users.models import Departments,User, DoctorProfile


from datetime import date


@login_required(login_url="/users/login/")
def appointment(request):
    doctors=User.objects.filter(role="DOCTOR")
    context={
        'doctors':doctors,
        
    }
    
    if request.method == 'POST':
        patient_name= request.POST.get('patient_name')
        patient_age= request.POST.get('patient_age')
        patient_email=request.POST.get('patient_email')
        patient_phone=request.POST.get('patient_phone')
        patient_gender= request.POST.get('patient_gender')
        appointment_date= request.POST.get('date')
        
        doctor= request.POST.get('doctor_id')
        doctor_name=User.objects.get(id=doctor)
        doctorName=doctor_name.name
        
        user_id=request.user.id
        
        appointment=Appointment.objects.filter(appoinment_date=appointment_date, doctor_name=doctor).aggregate(Max('serial_number'))['serial_number__max']
        
        if not appointment:
            Appointment.objects.create(user_id=user_id,patient_name=patient_name,patient_age=patient_age,patient_email=patient_email,patient_gender=patient_gender,patient_phone=patient_phone,doctor_name=doctor_name,serial_number=1,appoinment_date=appointment_date).save()
            send_mail(
                "Appointment Details",
                "Congratulations Mr/Mrs. "+ patient_name +", You have taken a serial on "+str(appointment_date)+" of doctor Mr." +str(doctorName)+ ". Your Serial number is :  1.",
                "appointmentdoctor1@gmail.com",
                [patient_email],
                fail_silently=False,
            )
                          
            account_sid = 'ACe96aec894ba7878875d0e65af391dff1'
            auth_token = '9af7b15fc636e645569ae30a88729687'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
            from_='+12186703680',
            body='Congratulations Mr/Mrs. '+ patient_name+' , You have taken appointment of doctor'+doctorName+' on' + appointment_date +' Your serial is : 1',
            to='+88'+str(patient_phone)
             )

            print(message.sid)
        else:
            appointment+=1
            Appointment.objects.create(user_id=user_id,patient_name=patient_name,patient_age=patient_age,patient_email=patient_email,patient_gender=patient_gender,patient_phone=patient_phone,doctor_name=doctor_name,serial_number=appointment,appoinment_date=appointment_date).save()
            send_mail(
                "Appointment Details",
               "Congratulations Mr/Mrs. "+ patient_name +", You have taken a serial on "+str(appointment_date)+" of doctor Mr." +str(doctorName)+ ". Your Serial number is :  "+str(appointment),
                "appointmentdoctor1@gmail.com",
                [patient_email],
                fail_silently=False,
            )
            account_sid = 'ACe96aec894ba7878875d0e65af391dff1'
            auth_token = '9af7b15fc636e645569ae30a88729687'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
            from_='+12186703680',
            body='Congratulations Mr/Mrs. '+ patient_name+' , You have taken appointment of doctor'+doctorName+' on' + appointment_date +' Your serial is : 1',
            to='+88'+str(patient_phone)
             )

            print(message.sid)
            
        return redirect('appointment_list')
    return render(request,'patient_dashboard/appointment.html',context)

@login_required(login_url="/users/login/")
def appointment2(request,doctor):
    doctor= User.objects.get(id=doctor)
    context={
        'doctor':doctor,
    }
    
    if request.method == 'POST':
        patient_name= request.POST.get('patient_name')
        patient_age= request.POST.get('patient_age')
        patient_email=request.POST.get('patient_email')
        patient_phone=request.POST.get('patient_phone')
        patient_gender= request.POST.get('patient_gender')
        appointment_date= request.POST.get('date')
        
        doctor= request.POST.get('doctor_id')
        doctor_name=User.objects.get(id=doctor)
        doctorName=doctor_name.name
        
        user_id=request.user.id
        
        user_id=request.user.id
        
        appointment=Appointment.objects.filter(appoinment_date=appointment_date, doctor_name=doctor).aggregate(Max('serial_number'))['serial_number__max']
        
        if not appointment:
            Appointment.objects.create(user_id=user_id,patient_name=patient_name,patient_age=patient_age,patient_email=patient_email,patient_gender=patient_gender,patient_phone=patient_phone,doctor_name=doctor_name,serial_number=1,appoinment_date=appointment_date).save()
            send_mail(
                "Appointment Details",
                "Congratulations Mr/Mrs. "+ patient_name +", You have taken a serial on "+str(appointment_date)+" of doctor Mr." +str(doctorName)+ ". Your Serial number is :  1.",
                "appointmentdoctor1@gmail.com",
                [patient_email],
                fail_silently=False,
            )
            account_sid = 'ACe96aec894ba7878875d0e65af391dff1'
            auth_token = '9af7b15fc636e645569ae30a88729687'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
            from_='+12186703680',
            body='Congratulations Mr/Mrs. '+ patient_name+' , You have taken appointment of doctor'+doctorName+' on' + appointment_date +' Your serial is : 1',
            to='+88'+str(patient_phone)
             )

            print(message.sid)
             
        else:
            appointment+=1
            Appointment.objects.create(user_id=user_id,patient_name=patient_name,patient_age=patient_age,patient_email=patient_email,patient_gender=patient_gender,patient_phone=patient_phone,doctor_name=doctor_name,serial_number=appointment,appoinment_date=appointment_date).save()
            send_mail(
                "Appointment Details",
               "Congratulations Mr/Mrs. "+ patient_name +", You have taken a serial on "+str(appointment_date)+" of doctor Mr." +str(doctorName)+ ". Your Serial number is :  "+str(appointment),
                "appointmentdoctor1@gmail.com",
                [patient_email],
                fail_silently=False,
            )
            account_sid = 'ACe96aec894ba7878875d0e65af391dff1'
            auth_token = '9af7b15fc636e645569ae30a88729687'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
            from_='+12186703680',
            body='Congratulations Mr/Mrs. '+ patient_name+' , You have taken appointment of doctor'+doctorName+' on' + appointment_date +' Your serial is : 1',
            to='+88'+str(patient_phone)
             )

            print(message.sid)
            
        return redirect('appointment_list')
    
    return render(request,'patient_dashboard/appointment2.html',context)


def load_doctors(request):
    department_id=request.GET.get('department_id')
    user_id=DoctorProfile.objects.filter(department=department_id).values('user_id')
    for id in user_id:
        doctors=User.objects.filter(id=id['user_id'])
    context={
        'doctors':doctors
    }
    return render(request,'patient_dashboard/doctors.html',context)

@login_required(login_url='/users/login/')
def all_appointments(request):
    today = date.today()
    
    user=request.user.id
    
    appointments=Appointment.objects.filter(user_id=user,is_cancelled=0).order_by('-id')
    context={
        'appointments': appointments,
        'today':today,
    }
    return render(request,'patient_dashboard/all_appointments.html',context)



@login_required(login_url='/users/login/')
def delete_appointment(request,pk):
    appointment=Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('appointment_list')



@login_required(login_url='/users/login/')
def doctor_details(request):
    doctor_id=request.GET.get('doctor_id')
    user=User.objects.get(id=doctor_id)
    doctor=DoctorProfile.objects.filter(user_id=doctor_id)
    context={
        'doctor':doctor,
        'user':user
    }
    return render(request,'patient_dashboard/doctor_details.html',context)


@login_required(login_url='/users/login/')
def cancel_appointment(request,pk):
    appointment=Appointment.objects.get(id=pk)
    
    if request.method == 'POST':
        
        cancel = request.POST.get("appointment_status")
        appointment=Appointment.objects.get(id=pk)
        appointment.is_cancelled = 1
        appointment.save()
        send_mail(
        "Appointment Details",
        "Your appointment has been cancelled",
        "appointmentdoctor1@gmail.com",
        [appointment.patient_email],
        fail_silently=False,
        )
        
        
        return redirect('appointment_list')
        
        
        
    return render(request, 'patient_dashboard/cancel_appointment.html', {"appointment": appointment})
    


