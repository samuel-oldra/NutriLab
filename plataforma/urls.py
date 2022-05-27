from django.urls import path

from . import views

urlpatterns = [
    path('pacientes/', views.pacientes, name='pacientes'),
]
