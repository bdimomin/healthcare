from doctor.models import DoctorEducationalQualifications
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate
from users.models import DoctorProfile

# class DoctorStatusForm(forms.ModelForm):
#     class Meta:
#         model=Doctor
#         fields=['is_active']
        
# class DoctorRegistrationForm(UserCreationForm):
#     class Meta:
#         model=Doctor
#         fields=('bmdc_registration_number','name', 'email', 'phone','fees','about','doc_image','department','password1','password2')
        

# class DoctorLoginForm(forms.ModelForm):
#     password = forms.CharField(label="Password",widget=forms.PasswordInput)
#     class Meta:
#         model=Doctor
#         fields=('email', 'password')
        
#     def clean(self):
#         if self.is_valid():
#             email=self.cleaned_data['email']
#             password=self.cleaned_data['password']
            
#             if not authenticate(email=email,password=password):
#                 raise forms.ValidationError("Invalid Credentials")
            
            
class DoctorProfileUpdate(forms.ModelForm):
    class Meta:
        model=DoctorProfile
        exclude=('user',)
        
        



class DoctorEducationalQualificationsForm(forms.ModelForm):
    class Meta:
        model = DoctorEducationalQualifications
        exclude=['doctor_id']
        widgets = {
            'degree_start_year': forms.DateInput(attrs={'type': 'date'}),
            'degree_end_year': forms.DateInput(attrs={'type': 'date'}),
        }
        
            
            