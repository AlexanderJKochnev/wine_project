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