from django.shortcuts import render,redirect
from .models import RegistrationForm
from django.core.exceptions import ValidationError
import re
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import math, random 
from .tasks import MailSendFunction


def home(request):
    return render (request,'home.html')

def OTPgenerator() : 

	digits_in_otp = '0123456789'
	OTP = "" 
	length = len(digits_in_otp)
	for i in range(6) : 
		OTP += digits_in_otp[math.floor(random.random() * length)] 

	return OTP 
    

def otp_genrate(request):
    if request.method=="POST":
        otp=request.POST['name']
    
    return render(request,"genotp.html")


def create(request):
    if request.method=="POST":
        name=request.POST['name']
        dob=request.POST['dob']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password != confirm_password:
            raise ValidationError("password do not match")
        otp = OTPgenerator()
        obj=RegistrationForm.objects.create(name=name,dob=dob,email=email,password=password,confirm_password=confirm_password,otp=otp)
        obj.save()
        
        task = MailSendFunction.delay(otp,email)
        return redirect('otp')
    return render (request,"index.html")
        


def regList(request):  
    reg = RegistrationForm.objects.all()  
    return render(request,"list.html",{'reg':reg})  

def delete(request, id):
    
    obj = get_object_or_404(RegistrationForm, id = id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("list")
    return render(request, "delete.html")


def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        if RegistrationForm.objects.filter(email=email,password=password).exists():
            return redirect ('home')
            
        else :
            raise ValidationError("password does not match enter a valid password")
            
        return redirect('home')
    return render (request,"login.html")
    



