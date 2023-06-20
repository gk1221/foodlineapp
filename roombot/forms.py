from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Textfarm, Testfarm


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號:",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼:",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class EditTextForm(forms.ModelForm):
    CHOICES = [('Web', '網路'), ('Problem', '題目'), ('Money', '錢錢')]
    tag = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:

        model = Textfarm
        fields = ['title', 'tag', 'body', ]

class EditTestform(forms.ModelForm):
    

    class Meta:

        model = Testfarm
        fields = ['body' ]