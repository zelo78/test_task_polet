# Пустой проект на Django и DRF

Универсальный пустой шаблон для создания проектов на **Django** и **Django REST framework**.

## Запуск

1. Клонировать проект `git clone`
2. Создать и активировать виртуальное окружение, установить пакеты:
```shell
python3.9 -m venv venv
source ./venv/bin/activate
pip install -Ur requirements.txt
```
3. Переименовать файл `start.env` в `.env` (Он должен находится в корне проекта, рядом с `README.md`)
4. Создать и применить миграции, создать суперпользователя:
```shell
python project/manage.py makemigrations
python project/manage.py migrate
python project/manage.py createsuperuser
```
5. Запустить сервер:
```shell
python project/manage.py runserver
```

### Реализованные URL

- <http://127.0.0.1:8000/admin/> - интерфейс администрирования
- <http://127.0.0.1:8000/api/> - API интерфейс
- <http://127.0.0.1:8000/api/token/> - API авторизации

### Swagger/OpenAPI 2.0 specifications

- <http://127.0.0.1:8000/swagger/> - A swagger-ui view of your API specification 
- <http://127.0.0.1:8000/swagger.json> - A JSON view of your API specification 
- <http://127.0.0.1:8000/swagger.yaml> - A YAML view of your API specification
- <http://127.0.0.1:8000/redoc/> - A ReDoc view of your API specification 

### Авторизация

1. Получение токена
```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "oleg", "password": "12345678"}' \
  http://127.0.0.1:8000/api/token/
```
2. Авторизация с использованием токена
```shell
curl \
  -H "Authorization: Bearer <token>" \
  http://127.0.0.1:8000/api/users/
```

## Использованные библиотеки

- [Django](https://www.djangoproject.com/) v. 4.0.4
- [Django REST framework](https://www.django-rest-framework.org/) v. 3.13.1
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) v. 1.20.0 - Yet another Swagger generator. Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) v. 5.1.0 - Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework
- [python-dotenv](https://pypi.org/project/python-dotenv/) v. 0.20.0 - Reads key-value pairs from a `.env` file and can set them as environment variables
- [black](https://black.readthedocs.io/en/stable/) v. 22.3.0 - The uncompromising code formatter
 