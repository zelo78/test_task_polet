# Тестовое задание компании Полёт

## Задание

С использованием языка python3, фреймворков Django и DRF выполнить проектирование и реализовать приложение, реализующее следующую функциональность:

- аутентификация с использование имени пользователя и пароля;
- создания/редактирования/поиск записей ТС (транспортное средство);
- загрузки и выгрузки списка записей ТС в/из файлов формата csv, xlsx;
- авторизация доступа к методам АПИ.

Приложение должно состоять из набора веб-АПИ, работающего по REST.

Приложение не должно содержать интерфейса.

Модель ТС состоит из следующих полей:
- Марка
- Модель
- Цвет
- Регистрационный номер
- Год выпуска
- vin
- Номер СТС (свидетельство о регистрации)
- Дата СТС

Универсальный пустой шаблон для создания проектов на **Django** и **Django REST framework**.

## Установка

1. Клонировать проект в пустую папку:
```shell
git clone https://github.com/zelo78/DRF-project-template.git .
```

2. Создать и активировать виртуальное окружение, установить пакеты:
```shell
python3.9 -m venv venv
source ./venv/bin/activate
pip install -Ur requirements.txt
```

3. Копировать файл `start.env` как `.env` (Он должен находится в корне проекта, рядом с `README.md`)
```shell
cp start.env .env
```

4. Создать и применить миграции, создать суперпользователя:
```shell
python project/manage.py makemigrations
python project/manage.py migrate
python project/manage.py createsuperuser --username USER
```

## Запуск

Запустить сервер:
```shell
python project/manage.py runserver
```

## Реализованные URL

- <http://127.0.0.1:8000/admin/> - интерфейс администрирования
- <http://127.0.0.1:8000/api/> - API интерфейс
- <http://127.0.0.1:8000/api/token/> - API авторизации

### Swagger/OpenAPI 2.0 specifications

Доступны при установке `DEBUG = True`

- <http://127.0.0.1:8000/swagger/> - A swagger-ui view of your API specification 
- <http://127.0.0.1:8000/swagger.json> - A JSON view of your API specification 
- <http://127.0.0.1:8000/swagger.yaml> - A YAML view of your API specification
- <http://127.0.0.1:8000/redoc/> - A ReDoc view of your API specification 

### Авторизация

#### Авторизация с помощью *BasicAuthentication* 
```shell
curl \
  -X GET \
  -H "Content-Type: application/json" \
  -u USER:PASSWORD \
  http://127.0.0.1:8000/api/users/
```

#### Авторизация с помощью *JWT*

- создаём токен авторизации
```shell
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "USER", "password": "PASSWORD"}' \
  http://127.0.0.1:8000/api/token/
```

Получаем ответ вида
> {"refresh":"ey...I0","access":"ey...lQ"}

- авторизуемся с помощью токена:
```shell
curl \
  -X GET \
  -H "Authorization: Bearer ey...lQ" \
  http://127.0.0.1:8000/api/users/
```

## Использованные библиотеки

- [Django](https://www.djangoproject.com/) v. 4.0.4
- [Django REST framework](https://www.django-rest-framework.org/) v. 3.13.1
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) v. 1.20.0 - Yet another Swagger generator. Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) v. 5.1.0 - Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework
- [python-dotenv](https://pypi.org/project/python-dotenv/) v. 0.20.0 - Reads key-value pairs from a `.env` file and can set them as environment variables
- [black](https://black.readthedocs.io/en/stable/) v. 22.3.0 - The uncompromising code formatter
 