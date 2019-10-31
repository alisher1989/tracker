from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from accounts.models import Git



class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, label='Username')
    first_name = forms.CharField(max_length=100, required=False, label='First name')
    last_name = forms.CharField(max_length=100, required=False, label='Last name')
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput,
                               label='Password')
    password_confirm = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput,
                               label='Password confirm')
    email = forms.EmailField(required=True, label='Email')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('Username is already taken.', code='username_taken')
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('This email is already registered', code='registered_email')
        except User.DoesNotExist:
            return email

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_confirm')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if password_1 != password_2:
            raise ValidationError('Passwords do not match', code='password_do_not_match')
        if not (first_name or last_name):
            raise ValidationError('One of these First name or Last name fields should be filled')
        return self.cleaned_data


class UserChangeForm(forms.ModelForm):
    git = forms.CharField(label='Git profile')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'git']


class UserChangePasswordForm(forms.ModelForm):
    password = forms.CharField(label="Новый пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Старый пароль", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm']


