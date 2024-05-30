# FLASK_BLOG_API

FLASK_BLOG_API - это простое веб-приложение для управления блогом, написанное с использованием Flask.


# Установка приложения и необходимых зависимостей к нему

1. Склонируйте репозиторий:
git clone https://github.com/lightningrusleen/flask_blog_app

2. Перейдите в директорию проекта:
cd flask_blog_api

3. Создайте виртуальное окружение:
python -m venv venv

4. Активируейте виртуальное окружение
Для Windows: venv\Scripts\activate
Для MacOs и Linux: source venv/bin/activate

5. Установите зависимости:
pip install -r requirements.txt
В файле requirements.txt вписаны необходимые фреймворки, библиотеки и расширения для установки и запуска приложения
Flask==3.0.3
Flask-RESTful==0.3.10
Flask-SQLAlchemy==3.1.1
Flask-Migrate==2.6.0
Flask-HTTPAuth==4.8.0
Flask-JWT-Extended==4.6.0
psycopg2-binary==2.9.9
python-dotenv==1.0.1
SQLAlchemy==2.0.30
sqlparse==0.5.0



# Настройка базы данных

1. Отредактируййте файл конфигурации 'config.py', указав параметры базы данных.

2. Создайте базу данных:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade


# Запуск приложения

1. Запустите приложение:
flask run

2. Откройте браузер и перейдите по ссылке, которая вышла в терминале:
http://localhost:5000


# Использование API
Запросы:
-Создание поста: 'POST /post'
-Получение поста: 'Get /post/<post_id>'
-Обновление поста: 'PUT /post/<post_id>'
-Удаление поста: 'DELETE /post/<post_id>'

-Создание комментария: 'POST /comment'
-Получение комментария: 'GET /comment/<comment_id>'
-Обновление комментария: 'PUT /comment/<comment_id>'
-Удаление комментария: 'DELETE /comment/<comment_id>'
