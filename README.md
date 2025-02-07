##### _разработка Sayfullin R.R.
##### _исходник https://github.com/wesm/pydata-book
Материалы и блокноты IPython для книги «Python для анализа данных, 3-е издание» Уэса МакКинни

Инструкция актуальна для Linux-систем.
========================================================================================================================
Используемые технологии:
    python~=3.13.1

Скопируйте репозиторий с помощью команды:
    $ git clone https://github.com/RuslanSayfullin/pydata-book
Перейдите в основную директорию с помощью команды: 
    $ cd pydata-book
Создать и активировать виртуальное окружение: 
    $ python3 -m venv venv $ source venv/bin/activate (venv) $
Установить зависимости из файла requirements.txt: 
    $ pip install -r requirements.txt
Создать файл из уже установленных зависимостей:
    $ pip freeze > requirements.txt
Для запуска Jupyter выполните в терминале команду:
    $ jupyter notebook
