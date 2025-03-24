# FastAPI Web Server

## Описание проекта

Персональный веб сервер для телеграм бота, умного дома, интеграции с алисой

## Технологии

- Python 3.9+
- FastAPI
- SQLAlchemy
- Pydantic

## Установка и запуск

1. Клонировать репозиторий:
```bash
git clone https://github.com/Holdenqwas/web_server.git
cd web_server
```

2. Создать и активировать виртуальное окружение (рекомендуется):
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows
```

3. Установить зависимости:
```bash
pip install -r requirements.txt
```

4. Запустить приложение:
```bash
python main.py
```

Приложение будет доступно по адресу: http://127.0.0.1:8000

## Документация API

После запуска сервера доступны следующие страницы документации:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Переменные окружения

Создайте файл `.env` в корне проекта и укажите необходимые переменные:
```

HOST=127.0.0.1
PORT=5000
DEBUG=False

DB_URL=postgresql://user:password@localhost/dbname
EXPIRED_IN=525600
JWT_KEY=secret_key
IS_NEED_GENERATE_TOKEN=False
MY_NAME=login
IS_WINDOWS=True
```

## Структура проекта

```
project/
├── alembic/                 # Миграция БД
├── app/                     # Основное приложение
│   ├── routes/              # Эндпоинты API
│   ├── utils/               # Основные настройки и конфигурации
│   ├── models/              # Модели данных
│   ├── schemas/             # Pydantic схемы
│   ├── crud/                # Операции с данными
│   └── main.py              # Точка входа
├── .env                     # Переменные окружения
├── requirements.txt         # Зависимости
└── README.md                # Этот файл
```

## Docker command
```bash
docker build -t web_server:latest .
docker run -d -p 5000:5000 --name web_server_container web_server:latest
docker exec -ti web_server_container /bin/bash
docker rm web_server_container
```
