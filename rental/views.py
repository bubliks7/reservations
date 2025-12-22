from django.shortcuts import render

# Create your views here.

def rental_view(request):
    return render(request, "rental/rental.html")
