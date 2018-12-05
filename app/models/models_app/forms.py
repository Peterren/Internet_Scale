from django import forms
from .models import Product
from .models import Driver


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description','price','quantity']


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name','last_name','car_model', "password", "email", "username", "birthday"]