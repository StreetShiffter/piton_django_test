![Django](https://www.djangoproject.com/s/img/logos/django-logo-negative.svg )


# 🔖 Описание проекта:

Инструкция работы с джанго


# 📁 ОПИСАНИЕ ФАЙЛОВ DJANGO:
---------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------

- **manage.py** — это скрипт командной строки, созданный Django, который облегчает управление проектом. В этом файле определяются команды для выполнения различных задач: запуск сервера, миграции баз данных, создание приложений и многое другое.

		Комманды запука:
		python manage.py runserver - Запуск сервера разработки
		python manage.py migrate - Применение миграций
		python manage.py startapp app_name - Создание нового приложения

- **asgi.py** - содержит настройки для серверного интерфейса ASGI (Asynchronous Server Gateway Interface). ASGI используется для асинхронного сервера, предоставляя поддержку асинхронных веб-приложений.

- **wsgi.py** - содержит настройки для серверного интерфейса WSGI (Web Server Gateway Interface). WSGI используется для взаимодействия между вашим проектом Django и веб-сервером, таким как Gunicorn или uWSGI. Обычно этот файл не требует дополнительных настроек.

- **settings.py** - содержит все основные настройки вашего проекта Django. Эти настройки включают конфигурацию баз данных, установленные приложения, настройки статических файлов и многое другое.
		
```🛠️ПАРАМЕТРЫ:```
		
1. BASE_DIR — определяет корневую директорию проекта. Этот параметр используется для построения абсолютных путей внутри проекта.

2. SECRET_KEY — секретный ключ, используемый для криптографических подписей. Необходимо держать его в секрете.

3. DEBUG — включает или отключает режим отладки. Включен (True) только в процессе разработки. 
			При разворачивании на сервере обязательно установить значение False.	

4. AlOWED_HOSTS  — список доменных имен, которые могут обслуживаться вашим приложением. На сервере добавьте сюда ваш домен. 
				(используйте '*' для разрешения всех)		

5. INSTALLED_APPS — содержит список всех приложений, активированных в вашем проекте. 
				Этот список включает как встроенные приложения Django, так и ваши собственные(вписываем 'PRILOGENIE' и не забываем в конце ,).

6. MIDDLEWARE — список промежуточного ПО, которое обрабатывает входящие запросы и выходящие ответы.

7. ROOT_URLCONF — указывает на модуль маршрутизации, который будет использоваться для маршрутизации URL-адресов в проекте. 
			В данном случае это 'config.urls'

8. TEMPLATES — настройки шаблонизации. Здесь указывается шаблонный двигатель по умолчанию, директории для шаблонов и контекстные процессоры, 
				которые добавляют переменные в контекст шаблона.

9. WSGI_APPLICATION — указывает путь к WSGI-приложению. Это точка входа вашего приложения для совместимости с WSGI-серверами, такими как Gunicorn. 				Настройка необходима в основном при разворачивании на сервере.
				# WSGI-приложение
					WSGI_APPLICATION = 'config.wsgi.application'

10. AUTH_PASSWORD_VALIDATORS — список валидаторов, используемых для проверки надежности паролей пользователей.

11. LANGUAGE_CODE — устанавливает язык для проекта.

12. TIME_ZONE — устанавливает часовую зону для проекта. Пример для московского времени:
 
			TIME_ZONE = 'Europe/Moscow'
			USE_I18N — включает поддержку интернационализации.
			USE_L10N — включает поддержку локализации, применяя форматирование даты и времени.
			USE_TZ — включает поддержку временных зон.
 
			# Локализация (Localization)
				LANGUAGE_CODE = 'en-us'
				TIME_ZONE = 'UTC'
				USE_I18N = True
				USE_L10N = True
				USE_TZ = True

13. STATIC_URL — содержит информацию о URL для доступа к статическим файлам.

14. STATICFILES_DIR — это список директорий на диске, из которых будут подгружаться статические файлы.
 
			# Настройки статических файлов (Static files)
				STATIC_URL = '/static/'
				STATICFILES_DIRS = [BASE_DIR / 'static']

15.  MEDIA_URL — содержит информацию о URL для доступа к медиафайлам.
	
16.  MEDIA_ROOT — это директория на диске, где будут храниться медиафайлы, загружаемые пользователями.
 
			# Медиатека (Media)
				MEDIA_URL = '/media/'
				MEDIA_ROOT = BASE_DIR / 'media'


17. urls.py — определяет маршрутизацию для вашего проекта, связывая URL-адреса с соответствующими контроллерами (views).

*=======================================================================================================================*
ОПИСАНИЕ ФАЙЛОВ 'PRILOGENIE':

- migrations/ - Миграции — это механизм, позволяющий управлять изменениями в структуре базы данных. Каждый раз, когда вы вносите изменения в модели,
 вам нужно создать и применить миграции.

- admin.py — файл для регистрации моделей в административной панели Django. Это позволяет управлять данными через встроенный интерфейс администрирования.

- apps.py — файл с конфигурацией приложения. Django автоматически создает здесь классы, представляющие приложение:

			from django.apps import AppConfig

			class StudentsConfig(AppConfig):
    				default_auto_field = 'django.db.models.BigAutoField'
    				name = 'students'

- models.py — файл, содержащий определения моделей. Модели описывают структуру данных и включают поля и методы для обработки этих данных.

- tests.py — файл для написания тестов unittest.

- views.py — файл для создания контроллеров (представлений). Контроллеры обрабатывают запросы от клиента и возвращают ответы.

		from django.shortcuts import render
		from django.http import HttpResponse - вызов функций DJANGO

		request.method == 'GET'\'POST' - Проверка типа запроса
		return render(request, 'app/data.html') - Выполняется рендеринг шаблона data.html, если запрос является GET-запросом
		return HttpResponse('Данные отправлены')\("Метод не поддерживается", status=405) -  используется для возврата простого HTTP-ответа

		def show_item(request, item_id):
    		# Логика для обработки данных элемента с указанным ID
    		return render(request, 'app/item.html', {'item_id': item_id}) - Функция show_item — это контроллер. 
										Она будет обрабатывать запросы к адресу /app/item/...

**!!! urls.py — определяет маршрутизацию для вашего приложения(создаем вручную и ваши пути указываем в основной urls.py для масштабирования)**

		from django.contrib import admin
		from django.urls import path, include

			urlpatterns = [
    				path('admin/', admin.site.urls),
    				path('app/', include('app.urls')), - include(включаем ваш маршрут из модуля urls.py приложения app)
				]


**Основа кода urls.py из приложения app(пример):**
- from django.urls import path - Импортирует функцию path() из модуля django.urls
- from . import views - Импортирует модуль views.py из текущей директории (отсюда точка перед import)

	```
    urlpatterns = [
    		path('home/', views.home, name='home'),
    		path('about/', views.about, name='about'), - Определяет один маршрут (URL-паттерн):

				'home/'— часть URL, которую пользователь видит в браузере (например, http://yoursite.com/home/)
				views.home — указывает на функцию home в файле views.py, которая будет обрабатывать этот URL.
				name='home' — имя маршрута, которое можно использовать в шаблонах и других частях кода для ссылок вместо жёсткого написания URL

		path('item/<int:item_id>/', views.show_item, name='show_item')
		]
    ```

**path('item/<int:item_id>/', views.show_item, name='show_item') - часть URL item и параметр числа(int) которым является аргумент
								 контроллера (item_id) show_item**



*----------------------------------------------------------------------------------------------------------------------*

**📤 ПРИМЕР РАБОТЫ**

http://localhost:8000/app/item/7/ - пользователь заходит по адресу

Django смотрит в основной файл urls.py проекта

-Находит: path('app/', include('app.urls'))
-Значит, дальше проверяет app/urls.py

В app/urls.py он ищет совпадение для item/7/

-Находит маршрут: path('item/<int:item_id>/', views.show_item, name = show_item)
-Вызывает функцию views.show_item(request, item_id=7)
-Функция show_item() возвращает страницу item.html с номером 7

в шаблонах можно использовать name = show_item:
<a href="{% url 'show_item' item_id=5 %}">Перейти к элементу 5</a>







***НАСТРОЙКА И РАБОТА***


1. Создайте проект и установите poetry:


```
pip install --user poetry
poetry add ipython - инструмент для удобной работы с DJANGO SHELL
poetry add dotenv - импорт важных данных из файла .env
psycopg2 - удобная работа с БД
зpoetry add pillow - ImageField требует установленной библиотеки Pillow для работы с картинками
```


2. Установите инструменты для реализации магазина

[![Django](https://img.shields.io/badge/Django-3.2.0-%2311677A?logo=django&logoColor=white&style=flat&labelColor=black)](https://www.djangoproject.com/)
[![python-dotenv](https://img.shields.io/badge/python--dotenv-black?logo=envoy&logoColor=orange)]( https://pypi.org/project/python-dotenv/ )
[![psycopg2](https://img.shields.io/badge/psycopg2-%233178C6?logo=postgresql&logoColor=white)]( https://pypi.org/project/psycopg2/ )


КОМАНДЫ ДЛЯ ЗАПУСКА ФРЕЙМВОРКА И ПРИЛОЖЕНИЯ
```
poetry add django # Установка 
django-admin startproject config . # Старт нового проекта
django-admin startproject myproject # Старт нового приложения
python manage.py startapp PRILOGENIE - Создание приложения(при создании создается файл db.sqlite3 - его необходимо удалить, если не планируете его использование)

```

# ✒️ Использование
Основное использование приложения запускается из файла *manage.py*

⚠️ ВАЖНО ⚠️
```
python manage.py runserver 8080 # Запуск сервера
CTRL+С # Отключение сервера

python manage.py makemigrations PRILOGENIE - создание миграций БД
python manage.py migrate - применение миграций(запись в БД)

python manage.py migrate PRILOGENIE номер_миграции - откат нужной миграции
python manage.py migrate PRILOGENIE zero - откат всех миграций

python manage.py createsuperuser - дать суперпользователя для админки
При выполнении этой команды необходимо указать имя пользователя и пароль. Адрес электронной почты является опциональным параметром.

python manage.py shell - вход в Django shell НО!!!
```
**Чтобы Django shell был удобным в использовании, установите пакет ipython.**

    python manage.py shell -i ipython - последующий запуск
    Ctrl + D или Ctrl + Z - выход(аналогично exit(), quit())

**интерфейс ipython**
`
In [1]: from PRILOGENIE.models import MODUL1, MODUL2 - импортирование нужного класса в можделях
In [2]:	modul1 = MODUL1.objects.create(Первое_поле='Раз', Второе_поле='Два', Третье_поле='Три') - создание объектов модели
In [3]: mod1 = MODUL2.objects.create(Первое_поле='Раз', Второе_поле='Два', Третье_поле=modul1) - создание объектов модели и привязка к другой модели
In [4]: modul1.Второе_поле = '2' - редактирование конкретного поля модели
`



**Cоздание фикстур**
``
Кодировка -Xutf8(для корректной работы в windows) и отступом 4 пробела(--indent 4)
``

- python -Xutf8 manage.py dumpdata catalog.Products catalog.Category --output general_fixture.json --indent 4  - **общие Фикстуры**
-
- python -Xutf8 manage.py dumpdata catalog.Products --output products_fixture.json --indent 4 - **конкретноая фикстура 1 таблицы**
-
- python manage.py loaddata products_fixture_load.json --database=default --ignorenonexistent  -
    **загрузка с указанием БД из файла settings и указание игнорирования несуществующих полей**
```
Пример создания суперпользователя:

					Username (leave blank to use '...'): admin
					Email address: 
					Password: 
					Password (again): 
					   This password is too short. It must contain at least 8 characters.
					   This password is too common.
					Bypass password validation and create user anyway? [y/N]: y
					Superuser created successfully.
		http://127.0.0.1:8000/admin/ - админка на вашем сайте

```

```Шаблонные фильтры:```

- <p>{{ author.first_name|upper }}</p> - — преобразует строку в верхний регистр.
  
- <p>{{ author.first_name|lower }}</p> - — преобразует строку в нижний регистр.

- <p>Дата рождения: {{ author.birth_date|date:"d M Y" }}</p>  — форматирует дату рождения автора в формате 
"день месяц год". Например, если дата рождения"2023-07-01", она будет преобразована в"01 Jul 2023".

- <p>Количество авторов: {{ authors|length }}</p> — возвращает количество студентов в списке 
students

- <p>Комментарий: {{ authors.comment|default:"Комментарий отсутствует" }}</p> default
 — возвращает значение по умолчанию, если переменная пуста или отсутствует.

- <p>Описание: {{ student.description|truncatechars:100 }}</p>— сокращает текст до указанного количества символов.