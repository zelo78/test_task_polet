# Тестовое задание компании Полёт

## Задание

С использованием языка Python 3, фреймворков Django и DRF выполнить проектирование и реализовать приложение, реализующее следующую функциональность:

- аутентификация с использованием имени пользователя и пароля;
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
- VIN
- Номер СТС (свидетельство о регистрации)
- Дата СТС

## Решение

Решение тестового задания компании [Такси Полёт](https://www.taxipolet.ru/) с использованием **Django**, **Django REST framework**, **PostgreSQL**, **Docker**, **Docker-compose**.

### Установка

1. Клонировать проект в пустую папку:
```shell
git clone https://github.com/zelo78/test_task_polet.git .
```

2. Копировать файл `start.env` как `.env` (Он должен находится в корне проекта, рядом с `README.md`)
```shell
cp start.env .env
```

3. Создать и запустить контейнер (при запуске контейнера будут созданы и применены миграции):
```shell
docker-compose up -d --build
```

4. Создать суперпользователя:
```shell
docker exec -it p_app python manage.py createsuperuser --username USER
```

5. В целях тестирования, базу данных можно наполнить сгенерированными данными (транспортные средства)
```shell
docker exec -it p_app python manage.py populatebase 40
```

6. Остановить контейнер
```shell
docker-compose down
```

### Запуск

```shell
docker-compose up
``` 

### Аутентификация

Реализована `BasicAuthentication` (для работы с Browsable API) и `JWTAuthentication`

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

### Создание / редактирование / поиск записей ТС (транспортных средств)

- [x] `GET /api/vehicle/`
  - получение списка ТС (с пагинацией)
  - только для авторизованных пользователей
  - для облегчения поиска, возможна фильтрация по марке и модели ТС
  - реализована выгрузка списка ТС в формате `CSV` или `XLSX`

Получаем список записей вида

    {
      "count": 25,
      "next": "http://127.0.0.1:8000/api/vehicle/?page=2",
      "previous": null,
      "results": [
        {
          "url": "http://127.0.0.1:8000/api/vehicle/1/",
          "brand": "INFINITI",
          "model": "FX",
          "color": "Темно-голубой",
          "registration_number": "000D592 29",
          "year_of_manufacture": 2010,
          "vin": "U89KNNFJAZL2ZCDF7",
          "vehicle_registration_number": "7995333635",
          "vehicle_registration_date": "2014-06-17"
        },
        {
          "url": "http://127.0.0.1:8000/api/vehicle/2/",
          "brand": "Toyota",
          "model": "Tacoma Access Cab",
          "color": "Оранжево-красный",
          "registration_number": "Х013AО 173",
          "year_of_manufacture": 2010,
          "vin": "SDJ4JTUPDPCZFL6VL",
          "vehicle_registration_number": "1317598895",
          "vehicle_registration_date": "2015-12-18"
        }
     ]
    }

Примеры:
```shell
curl \
  -X GET \
  -u USER:PASSWORD \
  http://127.0.0.1:8000/api/vehicle/
```

С фильтрацией (возможна фильтрация по `brand` и `model`)
```shell
curl \
  -X GET \
  -u USER:PASSWORD \
  http://127.0.0.1:8000/api/vehicle/?brand=infiniti
```

Выгрузка как `CSV` (также возможна как `XLSX`)
```shell
curl \
  -X GET \
  -u USER:PASSWORD \
  http://127.0.0.1:8000/api/vehicle/?download=csv
```

Комбинация параметров: фильтрация и выгрузка как `XLSX` с сохранением в файл
```shell
curl \
  -X GET \
  -u USER:PASSWORD \
  'http://127.0.0.1:8000/api/vehicle/?download=xlsx&brand=infiniti' \
  --output vehicle_list.xlsx
```

- [x] `GET /api/vehicle/1/`
  - получение данных о ТС
  - только для авторизованных пользователей

Получаем запись вида

    {
      "url": "http://127.0.0.1:8000/api/vehicle/1/",
      "brand": "INFINITI",
      "model": "FX",
      "color": "Темно-голубой",
      "registration_number": "000D592 29",
      "year_of_manufacture": 2010,
      "vin": "U89KNNFJAZL2ZCDF7",
      "vehicle_registration_number": "7995333635",
      "vehicle_registration_date": "2014-06-17"
    }

Пример:
```shell
curl \
  -X GET \
  -u USER:PASSWORD \
  http://127.0.0.1:8000/api/vehicle/1/
```

- [x] `POST /api/vehicle/`
  - создание записи о ТС
  - только для авторизованных пользователей

Ожидает данные вида

    {
      "brand": "INFINITI",
      "model": "FX",
      "color": "Темно-голубой",
      "registration_number": "000D592 29",
      "year_of_manufacture": 2010,
      "vin": "U89KNNFJAZL2ZCDF7",
      "vehicle_registration_number": "7995333635",
      "vehicle_registration_date": "2014-06-17"
    }

Возвращает данные вновь созданной записи о ТС (как в GET detail)

Пример:
```shell
curl \
  -X POST \
  -u USER:PASSWORD \
  -H "Content-Type: application/json" \
  http://127.0.0.1:8000/api/vehicle/ \
  --data-raw '{"brand":"INFINITI","model":"FX","color":"Темно-голубой","registration_number":"000D592 29","year_of_manufacture":2010,"vin":"U89KNNFJAZL2ZCD13","vehicle_registration_number":"7995333635","vehicle_registration_date":"2014-06-17"}'
```

- [x] `POST /api/vehicle/from_csv/`
  - создание записи о ТС из файла в формате `CSV`
  - только для авторизованных пользователей

Ожидает файл, первая строка которого - заголовки колонок, среди них есть колонки со всеми полями модели ТС (то есть "brand", "model", "color", "registration_number", "year_of_manufacture", "vin", "vehicle_registration_number", "vehicle_registration_date"). 
Подойдёт файл, аналогичный полученному в методе `GET /api/vehicle/?download=csv`

Возвращает созданные записи о ТС, а также ошибочные данные с указанием причин ошибки.

Пример:
```shell
curl \
  -X POST \
  -u USER:PASSWORD \
  -F 'file=@/home/oleg/vehicles_list.csv' \
  "http://127.0.0.1:8000/api/vehicle/from_csv/" 
```

- [x] `POST /api/vehicle/from_xlsx/`
  - создание записи о ТС из файла в формате `XLSX`
  - только для авторизованных пользователей

Ожидает XLSX файл, на активной вкладке которого первая строка - заголовки колонок, среди них есть колонки со всеми полями модели ТС (то есть "brand", "model", "color", "registration_number", "year_of_manufacture", "vin", "vehicle_registration_number", "vehicle_registration_date"). 
Подойдёт файл, аналогичный полученному в методе `GET /api/vehicle/?download=xlsx`

Возвращает созданные записи о ТС, а также ошибочные данные с указанием причин ошибки.

Пример:
```shell
curl \
  -X POST \
  -u USER:PASSWORD \
  -F 'file=@/home/oleg/vehicles_list.xlsx' \
  "http://127.0.0.1:8000/api/vehicle/from_xlsx/" 
```

- [x] `PATCH /api/vehicle/1/`
  - изменение записи о ТС
  - только для авторизованных пользователей

Ожидает частичные данные вида 

    {
      "brand": "INFINITI",
      "model": "FX",
      "color": "Темно-голубой",
      "registration_number": "000D592 29",
      "year_of_manufacture": 2010,
      "vin": "U89KNNFJAZL2ZCDF7",
      "vehicle_registration_number": "7995333635",
      "vehicle_registration_date": "2014-06-17"
    }

Возвращает данные изменённой записи о ТС (как в GET detail)

- [x] `DELETE /api/vehicle/1/`
  - удаление записи о ТС
  - только для авторизованных пользователей

Пример:
```shell
curl \
  -X DELETE \
  -u USER:PASSWORD \
  http://127.0.0.1:8000/api/vehicle/7/
```

### Методы API

- Получение списка ТС

`GET /api/vehicle` 

- Фильтрация (по производителю, по марке)

`GET /api/vehicle/?brand=infiniti&model=fx`

- Получение списка ТС как `CSV` файла

`GET /api/vehicle/?download=csv`

- Получение списка ТС как Excel `XLSX` файла

`GET /api/vehicle/?download=xlsx`

- Получение данных о конкретном ТС

`GET /api/vehicle/1/`

- Создание ТС

`POST /api/vehicle/`

- Создание ТС из `CSV` файла

`POST /api/vehicle/from_csv/`

- Создание ТС из `XLSX` файла

`POST /api/vehicle/from_xlsx/`

- Редактирование ТС

`PATCH /api/vehicle/1/`

- Удаление ТС

`DELETE /api/vehicle/1/`

### Дополнительные URL

#### Интерфейс администрирования

<http://127.0.0.1:8000/admin/>

#### Browsable API

<http://127.0.0.1:8000/api/>

#### Swagger/OpenAPI 2.0 specifications

Доступны при установке `DEBUG = True`

- <http://127.0.0.1:8000/swagger/> - A swagger-ui view of your API specification 
- <http://127.0.0.1:8000/swagger.json> - A JSON view of your API specification 
- <http://127.0.0.1:8000/swagger.yaml> - A YAML view of your API specification
- <http://127.0.0.1:8000/redoc/> - A ReDoc view of your API specification 

## Использованные библиотеки

- [Django](https://www.djangoproject.com/) v. 4.0.5
- [Django REST framework](https://www.django-rest-framework.org/) v. 3.13.1
- [Django-filter](https://django-filter.readthedocs.io/en/stable/index.html) v 22.1 - Django-filter allows users to filter down a queryset based on a model’s fields 
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) v. 1.20.0 - Yet another Swagger generator. Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) v. 5.1.0 - Simple JWT provides a JSON Web Token authentication backend for the Django REST Framework
- [python-dotenv](https://pypi.org/project/python-dotenv/) v. 0.20.0 - Reads key-value pairs from a `.env` file and can set them as environment variables
- [black](https://black.readthedocs.io/en/stable/) v. 22.3.0 - The uncompromising code formatter
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) v. 3.0.10 - A Python library to read/write Excel 2010 xlsx/xlsm files
- [XlsxWriter](https://xlsxwriter.readthedocs.io/index.html) v. 3.0.3 - XlsxWriter is a Python module for writing files in the Excel 2007+ XLSX file format.
- [Pandas](https://pandas.pydata.org/docs/index.html) v 1.4.3 - Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
- [factory_boy](https://factoryboy.readthedocs.io/en/stable/index.html) v. 3.2.1 - factory_boy is a fixtures replacement based on thoughtbot’s factory_bot.
- [faker_vehicle](https://pypi.org/project/faker-vehicle/) v. 0.2.0 - faker_vehicle provides vehicle and machinery related fake data for testing purposes
- [flake8](https://flake8.pycqa.org/en/latest/) v. 4.0.1 - Tool For Style Guide Enforcement
 