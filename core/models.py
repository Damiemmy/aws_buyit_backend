from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    UserRole=(
        ('user','User'),
        ('vendor','Vendor'),
        ('admin','Admin')
    )
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    role=models.CharField(max_length=10,choices=UserRole,default='user')

    def __str__(self):
        return self.username


