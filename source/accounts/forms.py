from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True, label='First name')
    last_name = forms.CharField(max_length=100, required=True, label='Last name')
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput,
                               label='Password')
    password_confirm = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput,
                               label='Password confirm')

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        try:
            User.objects.get(first_name=first_name)
            raise ValidationError('This name is already taken', code='taken_name')
        except User.DoesNotExist:
            return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        try:
            User.objects.get(last_name=last_name)
            raise ValidationError('This last name is already taken', code='taken_last_name')
        except User.DoesNotExist:
            return last_name

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_confirm')
        if password_1 != password_2:
            raise ValidationError('Passwords do not match', code='password_do_not_match')
        return self.cleaned_data


