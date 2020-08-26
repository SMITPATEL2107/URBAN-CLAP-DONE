from django.db import models

# Create your models here

class User(models.Model):
    email = models.EmailField(unique= True)
    password = models.CharField(max_length = 20)
    otp = models.IntegerField(default = 459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    role = models.CharField(max_length = 10)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)

class technician(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    fullname=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)

class customer(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    fullname=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)

class Main(models.Model):
    address=models.CharField(max_length=50)
    role=models.CharField(max_length=50,default="service")
    phone=models.CharField(max_length=13,default=1234567890)
    email=models.EmailField(max_length=50)

class Conform(models.Model):
    email=models.EmailField(max_length=50)