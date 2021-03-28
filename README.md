# botifer


Создать файл в проекте .env со следующими полями:

* EMAIL_HOST=smtp.gmail.com  # smtp host пример gmail
* EMAIL_PORT=587  # порт 
* EMAIL_HOST_USER= # почта ...@gmail.com
* EMAIL_HOST_PASSWORD= # пароль
* GOOGLE_RECAPTCHA_SECRET_KEY=[получить тут](https://www.google.com/recaptcha/admin/create#list)

Так же понадобится docker для удобного запуска redis

[Docker](https://www.docker.com/)


```
$ docker run -d -p 6379:6379 redis
```

В папке проекта, в терминале выполнить следующие команды

```
$ pip install virtualenv
$ virtualenv 'название виртуального окружения', либо python3 -m venv 'название виртуального окружения'
$ venv 'название виртуального окружения'/Scripts(или bin для linux)/activate
$ pip install -r requirements.txt
$ docker run -d -p 6379:6379 redis
$ celery -A botifer worker -l INFO
$ python manage.py collectstatic
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

