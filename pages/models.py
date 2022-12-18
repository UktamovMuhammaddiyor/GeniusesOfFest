from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.

class CustomUser(AbstractUser):
    status = models.CharField(max_length=250, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)