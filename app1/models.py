from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Users():
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
