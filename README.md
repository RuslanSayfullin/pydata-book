##### _разработка Sayfullin R.R.

Инструкция актуальна для Linux-систем.
========================================================================================================================
Используемые технологии:
    python~=3.9
    Django~=4.1
    PostgreSQL

Скопируйте репозиторий с помощью команды:
$ git clone https://github.com/RuslanSayfullin/reckoning.git
Перейдите в основную директорию с помощью команды: 
$ cd reckoning

Создать и активировать виртуальное окружение:
========================================================================================================================
$ poetry env use python3.9
Установить зависимости:
$ poetry install 
Сохранить, адрес созданного виртуального окружения из вывода(рекомендуется)
$ poetry shell
(web-py3.9) $
Выход:
$ exit

Добавить в директорию reckoning/backend файл psw.py
========================================================================================================================
В данный файл, необходимо добавить две переменные:

secret_key = 'ваш секретный ключ'   # секретный ключ приложения
dbase_psw = 'ваш ключ к БД'         # Пароль для подключения к БД

Создание БД
========================================================================================================================
$ sudo su - postgres
Теперь запускаем командную оболочку PostgreSQL:
$ psql 

=# CREATE DATABASE reckoning;
=# CREATE USER portaluser WITH PASSWORD 'myPassword';
=# GRANT ALL PRIVILEGES ON DATABASE reckoning TO portaluser;
=# \q
$ exit

Перейти в директорию reckoning
========================================================================================================================
Для запуска выполнить следующие команды:
Команда для создания миграций приложения для базы данных
$ python3 manage.py makemigrations
$ python3 manage.py migrate

Создание суперпользователя
$ python3 manage.py createsuperuser

Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:
по умолчанию почта admin@admin.com пароль: 12345

Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.

Команды для запуска приложения:
$ python3 manage.py runserver


Django-приложение будет доступно по адресу: http://127.0.0.1:8000/


# как подключиться по SSH
========================================================================================================================
SSH - это основной протокол для удаленного управления серверами на базе операционной системы Linux. 
Все действия при подключении к SSH выполняются в командной строке, при достаточном уровне знаний и привилегий в системе 
там можно сделать практически все, в отличие от FTP где можно только передавать и редактировать файлы.

Данные для подключения по SSH в Linux:
$ ssh cryptolis@ip_adress -p 22
http://ip_adress:8000/

разорвать соединение:
$ exit

========================================================================================================================

/home/rusl4n/.cache/pypoetry/virtualenvs/reckoning-DdNRBDmP-py3.11/bin/python


dicting = {"1": {"spec_nomination": "\u043a\u0443\u0445\u043e\u043d\u043d\u044b\u0439 \u0433\u0430\u0440\u043d\u0438\u0442\u0443\u0440", "spec_price": "10000", "spec_discounted_price": "9000"}, "2": {"spec_nomination": "\u041c\u043e\u0434\u0443\u043b\u044c\u043d\u044b\u0439 \u0434\u0438\u0432\u0430\u043d \u042d\u0433\u043e", "spec_price": "5000", "spec_discounted_price": "4000"}, "3": {"spec_nomination": "\u0428\u043a\u0430\u0444", "spec_price": "3000", "spec_discounted_price": "2500"}}

{"1": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "2": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "3": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "4": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "5": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "6": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "7": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "8": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "9": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "10": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "11": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "12": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "13": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "14": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "15": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}}