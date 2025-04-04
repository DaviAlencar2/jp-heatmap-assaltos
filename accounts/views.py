from django.shortcuts import render
from .forms import LoginForms

def login(request):
    form = LoginForms()
    return render(request, 'accounts/login.html', {'form': form, 'in_login_or_signup': True})

def signup(request):
    return render(request, 'accounts/signup.html')