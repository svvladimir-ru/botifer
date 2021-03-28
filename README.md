# botifer


Создать файл в проекте .env со следующими полями:

* DB_ENGINE=django.db.backends.postgresql_psycopg2 # указываем, что работаем с postgresql
* DB_NAME=# имя базы данных
* DB_USER=# логин для подключения к базе данных
* DB_PASSWORD=# пароль для подключения к БД (установите свой)
* DB_HOST=127.0.0.1 # название сервиса (контейнера)
* DB_PORT=5432 # порт для подключения к БД
* EMAIL_HOST=smtp.gmail.com  # smtp host пример gmail
* EMAIL_PORT=587  # порт 
* EMAIL_HOST_USER= # почта ...@gmail.com
* EMAIL_HOST_PASSWORD= # пароль
* GOOGLE_RECAPTCHA_SECRET_KEY=[google](https://www.google.com/recaptcha/admin/create#list)
