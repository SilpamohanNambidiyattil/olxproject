from django import forms
from sale.models import Vehicles
from django.contrib.auth.models import User

class VehiclesCreateForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields="__all__"
        widgets={
            "vehicle_name":forms.TextInput(attrs={"class":"form-control"}),
            "vehicle_number":forms.TextInput(attrs={"class":"form-control"}),
            "vehicle_model":forms.TextInput(attrs={"class":"form-control"}),
            "owner_name":forms.TextInput(attrs={"class":"form-control"}),
            "km_runs":forms.TextInput(attrs={"class":"form-control"})
        }

class VehiclesUpdateForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields = ["owner_name","km_runs","image"]
        widgets={
            "owner_name":forms.TextInput(attrs={"class":"form-control"}),
            "km_runs":forms.TextInput(attrs={"class":"form-control"}),
           
        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }

class LogInForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))