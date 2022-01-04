from django.db import models
from django.db.models.fields import NullBooleanField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser    
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager,
)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    
    objects = UserManager()
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    
    is_consumidor = models.BooleanField(default=False)
    is_cempresa = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    
    cuit = models.IntegerField(null=True, blank=True)
    domicilio = models.CharField(max_length=100, null=True, blank=True)
    codigoPostal = models.IntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=20)
    REQUIRED_FIELDS = []

class ConsumidorFinal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    def __str__(self):
        return self.user.email

class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    razonSocial = models.CharField(max_length=100)
    rubro = models.CharField(max_length=100)
    def __str__(self):
        return self.user.email