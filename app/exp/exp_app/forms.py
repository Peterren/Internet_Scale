from django import forms


class DriverForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)
    car_model = forms.CharField(label="Car Model", max_length=30)
    password = forms.CharField(max_length=20)
    email = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    birthday = forms.DateField(help_text='Format: m/d/yy')
    # id = forms.IntegerField(label = "ID")
