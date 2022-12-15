# Foodgram

## Описание

Приложение «Продуктовый помощник»: сайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволяет пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.А перед походом в магазин можно скачать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

![example workflow](https://github.com/BearLikesVodka/foodgram-project-react/actions/workflows/main.yml/badge.svg)

### Технологии

- Python 3.8;
- Django 3.2.16;
- Django Rest Framework 3.12.14;
- Docker;
- Djoser;
- Yandex.Cloud;
- PostgreSQL.

### Особенности

- применены вьюсеты;
- для аутентификации использованы возможности djoser;
- у неаунтефицированных пользователей доступ к API только на чтение;
- для загрузки проекта применён Docker, подготовлены файлы для развертывания инфраструктуры;
- настроены CI/CD.

### Установка

1. Клонировать репозиторий:

```bash
git clone github.com@BearLikesVodka/foodgram-project-git
```

2. В директории foodgram-project-react/infra создаём файл .env и записываем в него следующие переменные окружения:

```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<имя базы данных>
POSTGRES_USER=<ваш логин для подключения к базе данных>
POSTGRES_PASSWORD=<ваш пароль для подключения к базе данных>
DB_HOST=<название сервиса/контейнера>
DB_PORT=<порт для подключения к базе данных>
```

3. В директории foodgram-project-react/infra/ выполняем команду для сборки контейнеров:

```bash
docker compose up -d --build
```

4. Внутри собранных контейнеров создаём и выполняем миграции, создаём суперпользователя и собираем статику:

```bash
docker compose exec web python manage.py makemigrations 
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py collectstatic --no-input
```

- проект доступен по адресу http://<IP вашей машины>/

Полный список эднпоинтов при развернутом проекте приведен по адресу: ...api/docs/redoc/
