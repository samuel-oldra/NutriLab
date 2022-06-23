# Aplicação usando Python e Django 4

## NutriLab - PyStack Week 4.0

Aplicação para nutricionistas e pacientes.

Desenvolvida uma aplicação completa para nutricionistas gerenciarem seus pacientes.

## Tecnologias e práticas utilizadas
- Python
- Django 4
- SQLite
- Arquitetura MVT

## Funcionalidades
- Autenticação, Cadastro e Ativação de Usuários
- Gestão de Pacientes e seus Dados Laboratoriais

###

![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/logar.png)
![alt text](https://raw.githubusercontent.com/samuel-oldra/NutriLab/main/README_IMGS/cadastre-se.png)
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
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
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
