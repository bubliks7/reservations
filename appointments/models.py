from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Samochod(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    rok = models.IntegerField()
    cena_za_dzien = models.IntegerField()
    dostepnosc = models.BooleanField(default=True)
    opis = models.TextField()
    zdjecie = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return f"{self.marka} - {self.model} - {self.rok}"
    
class Rezerwacja(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Oczekuje'),
        ('confirmed', 'Potwierdzona'),
        ('cancelled', 'Anulowana'),
    ]

    klient = models.ForeignKey(User, on_delete=models.CASCADE)
    auto = models.ForeignKey(Samochod, on_delete=models.CASCADE)
    data_od = models.DateField()
    data_do = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    cena_ogolna = models.FloatField()
    data_utworzenia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.auto} - {self.data_od} - {self.data_do}"
    