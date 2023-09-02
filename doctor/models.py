from django.db import models
# from django import forms
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from users.models import User

# class DoctorManager(BaseUserManager):
#     def create_user(self,email,name,phone,department,bmdc_registration_number,fees,about,password=None):
#         if not email:
#             raise ValueError("Email is required")
#         if not phone:
#             raise ValueError("Phone is required")
#         if not name:
#             raise ValueError("Name is required")
#         if not department:
#             raise ValueError("Department is required")
        
#         if not bmdc_registration_number:
#             raise ValueError("BM&DC Registration Number is required")
        
#         user =self.model(
#             email=self.normalize_email(email),
#             name=name,
#             phone=phone,
#             department=department,
#             bmdc_registration_number=bmdc_registration_number,
#             fees=fees,
#             about=about
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    

# class Doctor(AbstractBaseUser):
#     email = models.EmailField(max_length=100, verbose_name="Email Address",unique=True)
#     name = models.CharField(max_length=100, verbose_name="Name")
#     phone=models.CharField(max_length=20, verbose_name="Phone", unique=True)
#     fees= models.CharField(max_length=6, verbose_name="Fees")
#     about=models.TextField()
#     # department=models.ForeignKey(Departments,verbose_name="Department", on_delete=models.CASCADE, related_name='department')
#     bmdc_registration_number=models.CharField(max_length=50,verbose_name="BM&DC Registration Number",unique=True)
#     doc_image = models.ImageField(upload_to="images/doctor/", default='images/doctor/avatar.webp')
    
#     date_joined=models.DateTimeField(auto_now_add=True)
#     last_login=models.DateTimeField(auto_now=True)
#     is_admin=models.BooleanField(default=False)
#     is_active=models.BooleanField(default=False)
#     is_staff=models.BooleanField(default=False)
#     is_superuser=models.BooleanField(default=False)
    
    
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS =['name','phone','department','bmdc_registration_number', 'fees','about']
    
#     objects=DoctorManager()
    
#     def __str__(self):
#         return self.name 

#     def has_perm(self, perm,obj=None):
#         return True
    
#     def has_module_perms(self, app_label):
#         return True
    
class DoctorEducationalQualifications(models.Model):
    doctor_id = models.ForeignKey(User,on_delete=models.CASCADE)
    degree_title = models.CharField(max_length=100,null=True,blank=True)
    degree_start_year = models.DateField(blank=True, null=True)
    degree_end_year = models.DateField(blank=True, null=True)
    university_name = models.CharField(max_length=100, null=True, blank=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.degree_title
