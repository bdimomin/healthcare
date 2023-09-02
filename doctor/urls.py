from django.urls import path
from doctor.views import *

urlpatterns = [
    # path('registration/',doctor_reg,name="doctor_registration"),
    # path('login/',doctor_login,name="doctor_login"),
    path('logout/',doctor_logout,name="doctor_logout"),
    path('home/',doctor_home,name="doctor_home"),
    path('profile/<int:pk>/',doctor_profile_update,name="doctor_profile_update"),
    path('appointment_list/<int:pk>/', appointment_list_view, name = "appointment_list_view"),
    path('<int:pk>/profile/',profile_doc, name = "profile_doc"),
    path('profile_details/',doctor_profile_details,name="Profile_details"),
]
