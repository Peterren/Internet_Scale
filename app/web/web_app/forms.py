from django import forms


class DriverForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=30)
    last_name = forms.CharField(label="Last Name", max_length=30)
    car_model = forms.CharField(label="Car Model", max_length=30)
    password = forms.CharField(max_length=20)
    email = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    birthday = forms.DateField(help_text='Format: m/d/yy')


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32, min_length=3)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    remember = forms.BooleanField(label='Remember Me', required=False)


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=32, min_length=3, help_text='At least 3 characters')
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, help_text='At least 8 characters')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, help_text='Re-enter password')
    birthday = forms.DateField(help_text='Format: m/d/yy')
    email = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'Password does not match')
        return cleaned_data
