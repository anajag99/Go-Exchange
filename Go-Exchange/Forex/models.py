from django.db import models

# Create your models here.
class login(models.Model):
    first_name=models.CharField(max_length=100,default="")
    last_name=models.CharField(max_length=100,default="")
    email_id=models.CharField(max_length=100,default="")
    country=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")
    city =models.CharField(max_length=100,default="")
    password=models.CharField(max_length=100,default="")
    confirmpassword=models.CharField(max_length=100,default="")
    
