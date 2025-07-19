from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=150,verbose_name='Имя')
    last_name = models.CharField(max_length=150,verbose_name='Afvbkbz')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        ordering = ['last_name']


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название книги')
    publication_date = models.DateField(verbose_name='Дата публикации')
    authors = models.ManyToManyField(Author, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        ordering = ['title']
