# drf-upload-test

Teste de upload de arquivos com Django REST framework.

## Este projeto foi feito com:

* [Python 3.10.6](https://www.python.org/)
* [Django 4.2](https://www.djangoproject.com/)
* [Django Rest Framework 3.14.0](https://www.django-rest-framework.org/)
* [dr-yasg](https://drf-yasg.readthedocs.io/en/stable/)
* [Djoser](https://djoser.readthedocs.io/en/latest/)

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

Upload

```
curl -X POST -H 'Authorization: Token <YOUR_TOKEN>' -F '<FIELD_NAME>=@<FILE.zip>' http://localhost:8000/api/v1/documentos/

curl -X POST -H 'Authorization: Token ac8542e61e6b48098ba9af900dad6d90caf2bde5' -F 'document=@doc01.pdf' http://localhost:8000/api/v1/documentos/
```

Autenticação

```
# Cria novo usuário
curl -X POST http://localhost:8000/api/v1/users/ --data 'username=djoser&password=api127rg'

# Login
curl -X POST http://localhost:8000/api/v1/auth/token/login/ --data 'username=djoser&password=api127rg'

# Informações do usuário
curl -X GET http://localhost:8000/api/v1/users/me/ -H 'Authorization: Token ac8542e61e6b48098ba9af900dad6d90caf2bde5'  # o seu será um novo

# Logout
curl -X GET http://localhost:8000/api/v1/auth/token/logout/ -H 'Authorization: Token ac8542e61e6b48098ba9af900dad6d90caf2bde5'  # o seu será um novo
```

## Links

https://www.django-rest-framework.org/api-guide/authentication/

https://djangotricks.blogspot.com/2020/03/how-to-upload-a-file-using-django-rest-framework.html

