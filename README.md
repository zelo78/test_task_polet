# Пустой проект на Django и DRF

Универсальный пустой шаблон для создания проектов на Django и Django REST framework.

## Реализованные URL

- <http://127.0.0.1:8000/admin/> - интерфейс администрирования
- <http://127.0.0.1:8000/api/> - API интерфейс
- <http://127.0.0.1:8000/api/token/> - API авторизации

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
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) v. 5.1.0 - Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework
- [python-dotenv](https://pypi.org/project/python-dotenv/) v. 0.20.0 - Reads key-value pairs from a `.env` file and can set them as environment variables
- [black](https://black.readthedocs.io/en/stable/) v. 22.3.0 - The uncompromising code formatter
 