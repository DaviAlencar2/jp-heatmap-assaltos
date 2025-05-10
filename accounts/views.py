from django.shortcuts import render, redirect
from .forms import LoginForms, SignupForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def login(request):
    is_htmx = request.headers.get('HX-Request') == 'true'
    template = 'partials/accounts/_loginForm.html' if is_htmx else 'accounts/login.html'

    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('home')
            else:
                messages.error(request,'Senha incorreta!')
    
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")

    else:
        form = LoginForms()

    return render(request, template, {'form': form})


def signup(request):
    is_htmx = request.headers.get('HX-Request') == 'true'
    template = 'partials/accounts/_signupForm.html' if is_htmx else 'accounts/signup.html'

    if request.method == 'POST':
        form = SignupForms(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')

            user = User.objects.create_user(
                username=username, 
                password=password, 
                email=email
            )

            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = SignupForms()
    
    return render(request, template, {'form': form,})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('home')