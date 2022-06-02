from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import render, redirect

from .models import Pacientes


@login_required(login_url='/auth/logar/')
def pacientes(request):
    if request.method == "GET":
        return render(request, 'pacientes.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        if ((len(nome.strip()) == 0) or (len(sexo.strip()) == 0) or (len(idade.strip()) == 0)
            or (len(email.strip()) == 0) or (len(telefone.strip()) == 0)):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/pacientes/')

        if not idade.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite uma idade válida')
            return redirect('/pacientes/')

        pacientes = Pacientes.objects.filter(email=email)
        if pacientes.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um paciente com esse e-mail')
            return redirect('/pacientes/')

        try:
            paciente = Pacientes(nome=nome, sexo=sexo, idade=idade, email=email, telefone=telefone, nutri=request.user)
            paciente.save()

            messages.add_message(request, constants.SUCCESS, 'Paciente cadastrado com sucesso')
            return redirect('/pacientes/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/pacientes/')
