from django.shortcuts import render, redirect
from .forms import LoginForms, SignupForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def login(request):
    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            username = form["username"].value()
            password = form["password"].value()

            user = auth.authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('home')
            
            else :
                messages.error(request, 'Usuário ou senha inválidos.')
                return render(request, 'accounts/login.html', {'form': form, 'in_login_or_signup': True})
            
        else:
            messages.error(request, 'Formulário inválido.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro em {field}: {error}")
            return render(request, 'accounts/login.html', {'form': form, 'in_login_or_signup': True})
            
    if request.method == "GET":
        form = LoginForms()
        return render(request, 'accounts/login.html', {'form': form, 'in_login_or_signup': True})


def signup(request):
    if request.method == 'POST':
        form = SignupForms(request.POST)

        if form.is_valid() and form["password"].value() == form["confirm_password"].value():

            username = form["username"].value()
            password = form["password"].value()
            email = form["email"].value()

            checks = {
            "usuario" : User.objects.filter(username=username).exists(),
            "email" :  User.objects.filter(email=email).exists()
            }

        
            if not checks["usuario"] and not checks["email"]:
                user = User.objects.create_user(username, password=password, email=email)
                user.save()
                messages.success(request, 'Usuário criado com sucesso!')
                return redirect('login')
            
            else:
                for check in checks:
                    if checks[check]:
                        messages.error(request, f'{check} já cadastrado!')
                return redirect('signup')
        else:
            messages.error(request, 'Dados inválidos ou as senhas não conferem.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro em {field}: {error}")
            return render(request, 'accounts/signup.html', {'form': form, 'in_login_or_signup': True})

    elif request.method == 'GET':
        form = SignupForms()
        return render(request, 'accounts/signup.html', {'form': form, 'in_login_or_signup': True})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('home')