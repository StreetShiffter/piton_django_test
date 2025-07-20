from django.contrib import admin
from .models import  Author, Book #точка нужна для поиска в своей директории, а не в корне проекта

#admin.site.register(Author) - самый простой способ админки без настроек

@admin.register(Author)# Регистратор в админке в виде декоратора
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)# Отображение объектов в админке
    list_filter = ('last_name',)# Фильтрация объектов в админке
    search_fields = ('first_name', 'last_name')# Поиск объектов в админке('author__book' - поиск по связаным моделям)
    ordering = ('last_name', 'first_name')  # Сортировка по возрастанию, '-last_name' - по убыванию
    fields = (('first_name', 'last_name'), 'birth_date')# Поля, которые будут отображаться на странице редактирования объекта. Можно группировать.
    #exclude = ('birth_date',) - Исключает указанные поля из формы редактирования.
    #readonly_fields = ('birth_date',)# Поля, которые нельзя редактировать (только просматривать)
    list_per_page = 25#  Количество записей на одной странице списка.
    #save_on_top = True# Отображает кнопки "Сохранить", "Сохранить и продолжить" и т.д. вверху формы.
    date_hierarchy = 'birth_date' #Добавляет навигацию по дате (вверху списка, как фильтр по дате).


@admin.register(Book) # Регистратор в админке в виде декоратора
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors')
    list_filter = ('publication_date',)
    search_fields = ('year',)



