from django import forms
from django.contrib.auth.models import User

class RejestracjaForm(forms.ModelForm):
    login = forms.CharField(max_length=150, label='Nazwa użytkownika')
    haslo = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    potwierdz_haslo = forms.CharField(widget=forms.PasswordInput, label="Potwierdź hasło")
    imie = forms.CharField(max_length=75, label='Imię')
    nazwisko = forms.CharField(max_length=80, label='Nazwisko')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['login', 'haslo', 'potwierdz_haslo', 'imie', 'nazwisko', 'email']
    
    def clean(self):
        wyczyszczone = super().clean()
        haslo = wyczyszczone.get('haslo')
        potwierdz_haslo = wyczyszczone.get('potwierdz_haslo')

        if haslo and potwierdz_haslo and haslo != potwierdz_haslo:
            raise forms.ValidationError('Hasla musza byc takie same')
        return wyczyszczone

    def save(self, commit=True):
        uzytkownik = User.objects.create_user(
            username=self.wyczyszczone['login'],
            password=self.wyczyszczone['haslo'],
            first_name=self.wyczyszczone['imie'],
            last_name=self.wyczyszczone['nazwisko'],
            email=self.wyczyszczone['email']
        )
        if commit:
            uzytkownik.save()
        return uzytkownik