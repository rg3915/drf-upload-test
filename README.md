# drf-upload-test

Teste de upload de arquivos com Django REST framework.

## Este projeto foi feito com:

* [Python 3.10.6](https://www.python.org/)
* [Django 4.1.5](https://www.djangoproject.com/)
* [Django Rest Framework 3.14.0](https://www.django-rest-framework.org/)
* [Bootstrap 4.0](https://getbootstrap.com/)
* [VueJS 3.2.13](https://vuejs.org/)
* [jQuery 3.4.1](https://jquery.com/)
* [htmx](https://htmx.org)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/drf-upload-test.git
cd drf-upload-test

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python contrib/env_gen.py

python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

## Links

https://www.django-rest-framework.org/api-guide/authentication/

https://djangotricks.blogspot.com/2020/03/how-to-upload-a-file-using-django-rest-framework.html

