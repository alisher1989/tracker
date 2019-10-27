from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True, label='First name')
    last_name = forms.CharField(max_length=100, required=True, label='Last name')
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput,
                               label='Password confirm')

