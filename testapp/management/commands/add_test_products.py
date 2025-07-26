from django.core.management.base import BaseCommand
from testapp.models import Author, Book


class Command(BaseCommand):
    help = 'Add test book in database'

    def handle(self, *args, **kwargs):
        # чистим все товары из БД
        Book.objects.all().delete()

        #Получаем всех авторов из модели Author
        author1, _ = Author.objects.get_or_create(last_name='Толстой')
        author2, _ = Author.objects.get_or_create(last_name='Пупкин')
        author3, _ = Author.objects.get_or_create(last_name='Жидкий')

        books = [
            {"title": "Кавказкий пленник", "publication_date": "1872", "authors": "", "category": author1},
            {"title": "Лучик", "publication_date": "2002", "authors": "", "category": author2},
            {"title": "Золотой дождь", "publication_date": "2018", "authors": "", "category": author3},
        ]

        # Перечисляем список словарей, получаем таблицу Book и делаем запись
        for book in books:
            product, created = Book.objects.get_or_create(**book)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Товар {book.title} успешно добавлен в базу!'))
            else:
                self.stdout.write(self.style.WARNING(f'Выбранные товары {book.title} уже имеется в базе!'))
