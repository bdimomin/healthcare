from django.urls import path
from .views import  *


urlpatterns = [
    path('home/',homepage, name="homepage"),
    path('login/',login_view,name="myadmin_login"),
    path('applist/',date_doc_appointment,name="date_doc_appointment"),
    path('doctorlist/',doctor_list, name="listDoctor"),
    path('doctor/<int:pk>',edit_doctor, name="edit_doctor"),
    path('departments/',departments,name="departments"),
]
