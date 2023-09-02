from appointment.api.serializers import AppointmentSerializer
from appointment.models import Appointment
# from doctor.models import Doctor
from users.models import DoctorProfile

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class Appointment_list(generics.ListAPIView):
    serializer_class=AppointmentSerializer
    
    # permission_classes = [IsAdminUser]
    
    def get_queryset(self):
        bmdc=self.kwargs['bmdc']
        doc= DoctorProfile.objects.get(bmdc_registration_number=bmdc)
        doc_id = doc.id
        date=self.kwargs['date']
        return Appointment.objects.filter(doctor_name=doc_id,appoinment_date=date)