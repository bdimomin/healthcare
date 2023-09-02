from users.models import User, Doctor, Patient, Departments, DoctorProfile
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.contrib.auth.forms import UserCreationForm


class PatientForm(UserCreationForm):
    class Meta:
        model = Patient
        fields =('name', 'email', 'phone','password1','password2')
        

        
class DoctorForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields =('name', 'email', 'phone','password1','password2')
        
        
class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        exclude = ('user',)
        
# class LoginForm(forms.ModelForm):
#     password = forms.CharField(label="Password",widget=forms.PasswordInput)
#     class Meta:
#         model=User
#         fields=('email', 'password')
