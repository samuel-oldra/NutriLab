from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='/auth/logar/')
def pacientes(request):
    return HttpResponse('Olá')
