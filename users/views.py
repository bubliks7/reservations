from django.shortcuts import render, redirect
from .forms import RejestracjaForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Utworzono konto')
            return redirect('/login/')
    else:
        form = RejestracjaForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return render(request, 'users/warning.html')
