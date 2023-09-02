from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Patient
from users.models import User

class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model=Patient
        fields=('name', 'email', 'phone','password1','password2')



class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    class Meta:
        model=Patient
        fields=('email', 'password')
        
    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']
            
            if not authenticate(email=email,password=password):
                raise forms.ValidationError("Invalid Credentials")
            
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['id','name','email','phone']
            
