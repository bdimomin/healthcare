from django.urls import path
from .views import *

urlpatterns = [
    path('doctor/register/',doctor_registration,name="doctor_registration"),
    path('patient/register/',patient_registration,name="patient_registration"),
    path('login/',login_view,name="login_view"),
]
