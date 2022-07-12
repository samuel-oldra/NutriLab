from django.http import HttpResponse
from django.shortcuts import render


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        return HttpResponse(confirmar_senha)


def logar(request):
    return HttpResponse("Você está na página de login")
