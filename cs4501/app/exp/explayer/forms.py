from django import forms


class DriverForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)
    car_model = forms.CharField(label="Car Model", max_length=30)
    rating = forms.FloatField(label="Rating")
