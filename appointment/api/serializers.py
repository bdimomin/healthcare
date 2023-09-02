from appointment.models import Appointment
from rest_framework import serializers



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields=['serial_number','patient_name','patient_age','patient_gender','appoinment_date','doctor_name']
        
    def to_representation(self, instance):
        rep=super(AppointmentSerializer, self).to_representation(instance)
        rep['doctor_name']=instance.doctor_name.name
        return rep
        