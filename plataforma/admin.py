from django.contrib import admin

from .models import Pacientes, DadosPaciente

admin.site.register(Pacientes)
admin.site.register(DadosPaciente)
