from django.db import models

# Create your models here.

class RegistrationForm(models.Model):
    name = models.CharField(max_length=30,blank=False)
    dob = models.CharField(max_length=10,blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=30,blank=False)
    confirm_password = models.CharField(max_length=30,blank=False)
    otp = models.IntegerField(default=162012)
    
    
    def __str__(self):
        return self.name    



    