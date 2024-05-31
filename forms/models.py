from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

# Create your models here.
class reports(models.Model):
    Quality = models.SmallIntegerField()
    Date = models.DateTimeField()
    city = models.CharField(max_length=5)
class auth_user(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    def isvalid(self,username,password):
        if self.username == username and self.password==password:
            return True
        else:
            return False
    