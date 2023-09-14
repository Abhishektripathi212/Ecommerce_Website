from django.db import models
from ecommerce.constants.shops import *
from shop.models import BaseModel
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('username', email)

        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('username', email)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user


# Create your models here.
class User(AbstractUser, BaseModel):
    gender_choices = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    email = models.EmailField(_("email address"), unique=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    gender = models.CharField(max_length=300, blank=True, null=True, choices=gender_choices)
    dob = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.first_name:
            return ' '.join((self.first_name, self.last_name))
        else:
            return self.username

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'customers'

        indexes = [
            models.Index(fields=['id', 'deleted_at']),
        ]