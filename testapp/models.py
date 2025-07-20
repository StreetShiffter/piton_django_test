from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=150,verbose_name='Имя')
    last_name = models.CharField(max_length=150,verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        ordering = ['last_name']


class Book(models.Model):
    FIRST_YEAR = 'first'
    SECOND_YEAR = 'second'
    THIRD_YEAR = 'third'
    FOURTH_YEAR = 'fourth'# Константы для привязывания параметра(что бы не писать вручную и не писать с ошибками)

    YEAR_IN_PUBLICATE = [
        (FIRST_YEAR, 'Первый курс'),
        (SECOND_YEAR, 'Второй курс'),
        (THIRD_YEAR, 'Третий курс'),
        (FOURTH_YEAR, 'Четвертый курс'),
    ]


    title = models.CharField(max_length=200, verbose_name='Название книги')
    publication_date = models.DateField(verbose_name='Дата публикации')
    authors = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    year = models.CharField(
        max_length=6,
        choices=YEAR_IN_PUBLICATE,
        default=FIRST_YEAR,
        verbose_name='Публикация'
    )

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ['title']
