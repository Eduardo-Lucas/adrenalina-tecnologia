from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from apps.accounts.forms import CreateUserForm
from apps.funcionarios.models import Funcionario


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('empresas:painel_empresa')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                f = Funcionario(user=user,
                                nome=form.cleaned_data.get('username'),
                                email=form.cleaned_data.get('email'))
                f.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Uma conta foi criada para o usuário ' + user)

                return redirect('accounts:login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('empresas:painel_empresa')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Bem-vindo '+str(user)+'!')
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, 'Usuário ou senha está incorreto')

        context = {}
        return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Obrigado por usar a plataforma e volte logo!')
    return redirect('empresas:painel_empresa')
