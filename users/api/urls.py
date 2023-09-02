from django.urls import path
from users.api.views import DoctorList,OneDoctor,DepartmentList,OneDepartment,login_view,patient_details,get_patients

urlpatterns = [
    path('doctor/list/',DoctorList.as_view(),name='doctor_list'),
    path('doctor/<int:pk>/',OneDoctor.as_view(),name='one_doctor'),
    path('department/list/',DepartmentList.as_view(),name='doctor_list'),
    path('department/<int:pk>/',OneDepartment.as_view(),name='one_department'),
    path('doctor/login/', login_view, name='login'),
    
    path('patient/<int:pk>/',patient_details, name="patient_details"),
    path('patient/list/',get_patients, name="patient_list"),
]
