from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=true)
    is_active = models.BooleanField(default=true)
    is_staff = models.BooleanField(default=true)

