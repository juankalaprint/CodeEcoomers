from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, name, lastname, username, email,  password=None, **extra_fields):
        if not email:
            raise ValueError('el usuario debe tener un email')
        
        if not username:
            raise ValueError('el usuario debe tener un username')
        if not name:
            raise ValueError('el usuario debe tener un nombre')
        if not lastname:
            raise ValueError('el usuario debe tener un apellido')
        user = self.model(
            name=name,
            lastname=lastname,
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, lastname, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True) # Superuser debe estar activo
        extra_fields.setdefault('is_staff', True) # Superuser must have is_staff=True esta activo
        extra_fields.setdefault('is_superadmin', True)# Superuser must have is_superuser=True # tiene todos los permisos admin

        

        return self.create_user(name, lastname, username, email, password, **extra_fields)
    
'''class Auth(AbstractBaseUser, PermissionsMixin):'''

class Auth(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)

    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True) 
    is_superadmin = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'lastname']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' # para iniciar sesion
    REQUIRED_FIELDS = ['username', 'name', 'lastname'] # campos obligatorios

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True