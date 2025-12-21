from django.shortcuts import render, redirect
from .forms import RejestracjaForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Utworzono konto')
            return redirect('/')
    else:
        form = RejestracjaForm()
    return render(request, 'users/register.html', {'form': form})
