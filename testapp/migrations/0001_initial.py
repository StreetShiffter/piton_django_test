# Создаем структуру в БД при помощи python manage.py migrate

#Заполнение данными через админку в браузере python manage.py createsuperuser,
#через django shell python manage.py shell -i ipython, через фикстуру  python manage.py loaddata author_fixture.json --format json


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'автор',
                'verbose_name_plural': 'авторы',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название книги')),
                ('publication_date', models.DateField(verbose_name='Дата публикации')),
                ('year', models.CharField(choices=[('first', 'Первый курс'), ('second', 'Второй курс'), ('third', 'Третий курс'), ('fourth', 'Четвертый курс')], default='first', max_length=6, verbose_name='Публикация')),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='testapp.author')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
                'ordering': ['title'],
            },
        ),
    ]
