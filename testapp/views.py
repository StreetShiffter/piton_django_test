from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book

#Простой контроллер, отображающий страницу
def home(request):
    '''Загрузка стартовой страницы'''
    return render(request, 'home.html')

#Контроллер динамический - может возвращать данные из БД или собственные
def teach(request):
    '''Загрузка стартовой страницы'''
    author = Author.objects.get(id=1)
    book = Book.objects.get(id=1)
    #Передача отдельно поля объектов. В шаблоне надо указывать ключи
    # context = {
    #     'author_name': f'{author.first_name} {author.last_name}',
    #     'author_birth_date': author.birth_date,
    #     'book_name': book.title,
    #     'year': book.get_year_display(),
    # }

# Передаем поля объекта как метод(author.имя, author.фамилия, book.дата публикации и т.д.)
    #P.S. если поле имеет параметр choise, то при передаче в шаблон вместо book.year передать book.get_year_display,
    #то передается человекочитаемая инфа(работает как get_(имя_поля)_display)
    context = {
        'author': author,
        'book': book,
    }
    return render(request, 'teach.html', context)



def feedback(request):
    '''УНИВЕРСАЛЬНАЯ ФУНКЦИЯ ОТОБРАЖЕНИЯ И ОТПРАВКИ ФОРМЫ'''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')


