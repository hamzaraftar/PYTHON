from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.CharField(max_length=14)
    mobile = models.CharField(max_length=100)
    email_toke = models.CharField(max_length=100)
    forgot_password = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'