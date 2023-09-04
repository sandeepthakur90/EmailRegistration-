from django.contrib import admin
from .models import RegistrationForm

# Register your models here.
class registerAdmin(admin.ModelAdmin):
    list_display = ["name", "dob", "email","password","confirm_password","otp"]

admin.site.register(RegistrationForm, registerAdmin)



