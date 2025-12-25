from django.urls import path
from . import views

app_name = "rental"

urlpatterns = [
    path('create/<int:pk>', views.rezerwuj, name='rezerwuj'),
    path('myReservations/', views.mojeRezerwacje, name='mojeRezerwacje'),
]
