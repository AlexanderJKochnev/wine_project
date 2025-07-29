# wine_project
Структура проекта:

1. Postgresql: база данных 
   1. перенос данных на другой сервер:
     - docker exec -t your_postgres_container pg_dump -U postgres -Fc my_database > db_dump.dump
     - Перенести файл db_dump.dump на новый сервер.
     - cat db_dump.dump | docker exec -i new_postgres_container pg_restore -U postgres -d my_database
     - проверка
       - docker exec -it postgres_container psql -U postgres -c "\l"
       - docker exec -it postgres_container psql -U postgres -d my_database -c "SELECT count(*) FROM your_table;"
2. Adminer: сервис для просмотра базы данных (в продакшн можно отключить)
   1. как войти в сервис:
    - localhost:8082 (см. .env ADMINER_PORTS)
    - system: PostgreSQL
    - Server: wine_host (название сервиса postgresql в docker_compose.yaml)
    - Username: .env/POSTGRES_USER
    - Password: .env/POSTGRES_PASSWORD
    - Database: .env/POSTGRES_DB
3. App:  FastApi service
4. Alembic:  migration management
   1. Контролировать в файле alembic.ini строку подключения: Alembic не поддерживает asyncpg напрямую. Нужно использовать psycopg2 для миграций.
      1. sqlalchemy.url = driver://user:pass@localhost/dbname
      2. строка подключения в fastapi postgresql+asyncpg://user:password@localhost:5432/myappdb
      3. строка подключения в alembic sqlalchemy.url = postgresql://user:password@localhost:5432/myappdb
5. Docker: 
   1. Явно указать !/.env в .dockerignore
6. Админ панели
   1. http://localhost:8000/redoc redoc
   2. http://localhost:8000/docs swagger
   3. 