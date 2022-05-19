import email
from django.db import models

# Create your models here.

class Registration(models.Model):
    email = models.EmailField(primary_key=True)
    enabled = models.BooleanField(default=False)
    registration_type = models.CharField(max_length=30,null=False,blank=False)
    user_type = models.CharField(max_length=30,null=False,blank=False)

class ClientUserInvite(models.Model):
    email = models.EmailField(primary_key=True)
    client_code = models.CharField(max_length=30,null=False,blank=False)
    user_type=models.CharField(max_length=30,null=False,blank=False)
    accepted = models.BooleanField(default=False)
    role = models.CharField(max_length=30,null=False,blank=False)
    inviter = models.EmailField(blank=False,null=False)
   
