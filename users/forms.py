from django import forms
from django.contrib.auth.models import User

class RejestracjaForm(forms.ModelForm):
    login = forms.CharField(max_length=150, label='Nazwa użytkownika')
    haslo = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    potwierdz_haslo = forms.CharField(widget=forms.PasswordInput, label="Potwierdź hasło")
    imie = forms.CharField(max_length=75, label='Imię')
    nazwisko = forms.CharField(max_length=80, label='Nazwisko')
    email = forms.EmailField(label='Email')
