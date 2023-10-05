from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('provide valid email')
        NE=self.normalize_email(email)
        User=self.model(email=NE,first_name=first_name,last_name=last_name)
        User.set_password(password)
        User.save()
        return User
    def create_superuser(self,email,first_name,last_name,password):
        User=self.create_user(email,first_name,last_name,password)
        User.is_staff=True
        User.is_superuser=True
        User.save()
       

        
class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
    objects=UserProfileManager()