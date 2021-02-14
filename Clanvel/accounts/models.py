from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin 
)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, is_staff = False, is_admin = False, is_active=True):
        if not email:
            raise ValueError("Users must have an email address.")
        if not password:
            raise ValueError("Users must have a password")
        if not first_name:
            raise ValueError("Users must have a first name")
        user_obj = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name 
        )
        user_obj.set_password(password) # change user password 
        user_obj.staff = is_staff 
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.active = is_active 
        user_obj.admin = is_admin 
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, email, first_name, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff = True   
        )
        return user 
    
    def create_superuser(self, email, first_name, password):
        user = self.create_user(email, password)
        user.staff = True 
        user.admin = True 
        user.save()
        return user





class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # email and password are required by default 
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = UserManager() 

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

    def has_perms(self, perm, obj=None):
        return True 

    def has_module_perms(self, app_label):
        return True 

    @property 
    def is_staff(self):
        return self.staff 
    
    @property
    def is_superuser(self):
        return self.admin
    
    @property 
    def is_active(self):
        return self.active 

class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email