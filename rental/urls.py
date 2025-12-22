from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.rental_view, name='rental_view'),
]
