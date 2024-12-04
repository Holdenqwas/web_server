# Использование alembic


`alembic revision --autogenerate -m "fix"` - создать версию

`alembic upgrade head` - проапгрейдить базу до последнего состояния

`alembic stamp head`  to indicate that the current state of the database represents the application of all migrations