from rest_framework import serializers
from users.models import User, DoctorProfile, Departments
from django.contrib.auth.hashers import make_password

class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Departments
        fields=['id','name']
    
class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields=['id','name','email','phone']
        
class DoctorProfileSerializer(serializers.ModelSerializer):
    department= serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = DoctorProfile
        fields=['bmdc_registration_number','department','fees','about']
        
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','phone']
        

        