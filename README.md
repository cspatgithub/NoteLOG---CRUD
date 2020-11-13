# NoteLOG---CRUD
Github repository for the NoteLOG project on my youtube channel.

#### Clone project using:
git clone https://github.com/cspatgithub/NoteLOG---CRUD.git

#### Create a virtualenv for the project(Python virtualenv):
- py -m venv env
- env\scripts\activate
- pip install django django-crispy-forms

#### Run migrations and development server:
- cd src
- py manage.py makemigrations
- py manage.py migrate
- py manage.py createsuperuser
- py manage.py runserver

#### View project in browser:
http://127.0.0.1:8000/
