from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class PatientManager(BaseUserManager):
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
        

class Patient(AbstractBaseUser):
    email = models.EmailField(max_length=100, verbose_name="email address",unique=True)
    name = models.CharField(max_length=100, verbose_name="name")
    phone=models.CharField(max_length=20, verbose_name="phone", unique=True)
    
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
   
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =['name','phone']
    
    objects=PatientManager()
    
    def __str__(self):
        return self.name

    def has_perm(self, perm,obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    