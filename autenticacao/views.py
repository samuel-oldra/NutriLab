from django.http import HttpResponse


def cadastro(request):
    return HttpResponse("Você está na página de cadastro")


def logar(request):
    return HttpResponse("Você está na página de login")
