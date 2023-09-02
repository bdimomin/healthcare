from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class Departments(models.Model):
    name= models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class AdminUserManager(BaseUserManager):
    def create_user(self,email,name,phone,password=None):
        if not email:
            raise ValueError("Email is required")
        if not phone:
            raise ValueError("Phone is required")
        if not name:
            raise ValueError("Name is required")
        
        user =self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,phone,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            password=password
        )
        user.is_admin=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user
    
    

class User(AbstractBaseUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        PATIENT = "PATIENT", "Patient"
        DOCTOR = "DOCTOR", "Doctor"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)
    email = models.EmailField(max_length=100, verbose_name="email address",unique=True)
    name = models.CharField(max_length=100, verbose_name="name")
    phone=models.CharField(max_length=20, verbose_name="phone", unique=True)
    
    
    objects=AdminUserManager()
    
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =['name','phone']
    
    

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role            
            return super().save(*args, **kwargs)
        
    



class PatientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.PATIENT)


class Patient(User):
    base_role = User.Role.PATIENT
    patient = PatientManager()
    
    class Meta:
        proxy = True
    def welcome(self):
        return "Only for patient"



class DoctorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.DOCTOR)


class Doctor(User):
    base_role = User.Role.DOCTOR
    doctor = DoctorManager()
    class Meta:
        proxy = True
    def welcome(self):
        return "Only for doctors"
    
    
    
    
    
class DoctorProfile(models.Model):
    user= models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name='user')
    fees= models.CharField(max_length=6, verbose_name="Fees")
    about=models.TextField()
    department=models.ForeignKey(Departments,verbose_name="Department", on_delete=models.CASCADE, related_name='department')
    bmdc_registration_number=models.CharField(max_length=50,verbose_name="BM&DC Registration Number",unique=True)
    doc_image = models.ImageField(upload_to="images/doctor/", default='images/doctor/avatar.webp')
    

    def __str__(self):
        return self.bmdc_registration_number
    
    
