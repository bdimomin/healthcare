from django.shortcuts import render
# from doctor.models import Doctor, DoctorsProfile
from users.models import User, DoctorProfile


def frontpage(request):
    users= User.objects.filter(role="DOCTOR").all()
    doctors = DoctorProfile.objects.select_related('user').all()
    mylist=zip(users,doctors)
    context ={
        'mylist':mylist,
    }
    return render(request, 'frontpage/index.html',context)

