# Aplicação usando Python e Django 4.2

## NutriLab - PyStack Week 4.0

Aplicação para nutricionistas e pacientes.

Desenvolvida uma aplicação completa para nutricionistas gerenciarem seus pacientes.

## Tecnologias e práticas utilizadas
- Python 3.8
- Django 4.2
- SQLite
- Arquitetura MVT

## Funcionalidades
- Autenticação, Cadastro e Ativação de Usuários
- Gestão de Pacientes, seus Dados Laboratoriais e seus Planos Alimentares

###

![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/cadastre-se.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/logar.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/gerenciar_pacientes.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/novo_paciente.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/dados_dos_pacientes.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/dados_do_paciente.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/dados_do_paciente_detalhes.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/plano_alimentar_paciente.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/adicionar_refeicao.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/adicionar_opcao.png)

## Comandos

### pip
```
pip list --outdate
pip install --upgrade pip setuptools Django ...
```

### virtualenv (windows)
```
python -m venv env
env\Scripts\activate.bat
env\Scripts\deactivate.bat
```

### Instalar bibliotecas, gravar/instalar requerimentos
```
(env) pip install Django
(env) pip install Pillow

(env) pip freeze > requirements.txt
(env) pip install -r requirements.txt
```

### Criar projeto
```
(env) django-admin startproject nutrilab .
```

### Criar super user (Django Administration)
```
(env) python manage.py createsuperuser (admin/admin)
```

### Criar apps
```
(env) python manage.py startapp autenticacao
(env) python manage.py startapp plataforma
```

### Migrations
```
(env) python manage.py makemigrations
(env) python manage.py migrate
```

### Executar projeto
```
(env) python manage.py runserver
```