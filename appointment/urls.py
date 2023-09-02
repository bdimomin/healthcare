from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('',views.appointment,name="appointment"),
    path('<int:doctor>/',views.appointment2, name="appointment2"),
    path('list/',views.all_appointments,name='appointment_list'),
    path('delete/<int:pk>/',views.delete_appointment,name='delete_appointment'),
    
    path('load-doctor/', views.load_doctors, name='ajax_load_doctors'),
    path('doctor-details/', views.doctor_details, name='ajax_doctor_details'),
    
    path('cancel/<int:pk>/', views.cancel_appointment,name ='cancel_appointment'),
    
]
