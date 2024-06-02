from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

# Create your models here.
class reports(models.Model):
    Quality = models.SmallIntegerField()
    Date = models.CharField(max_length=11)
    city = models.CharField(max_length=5)

class auth_user(AbstractBaseUser):

        def __str__(self):
            return self.username