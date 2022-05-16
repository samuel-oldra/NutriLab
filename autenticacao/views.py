from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .utils import password_is_valid


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')

        # TODO: Verificar se username é único

        try:
            user = User.objects.create_user(username=username, email=email, password=senha, is_active=False)
            user.save()
            return redirect('/auth/logar')
        except:
            return redirect('/auth/cadastro')

        return HttpResponse(confirmar_senha)


def logar(request):
    return HttpResponse("Você está na página de login")