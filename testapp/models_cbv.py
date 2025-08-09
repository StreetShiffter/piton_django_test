from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    FormView,
    RedirectView,
)
from django import forms
from .models import Author, Book
from .forms import AuthorForm, BookForm  # Предполагаем, что формы созданы (можно использовать ModelForm)


# === 1. AuthorListView — Отображение списка авторов ===
class AuthorListView(ListView):
    model = Author  # Указывает модель, данные которой будут отображаться
    template_name = 'authors/author_list.html'  # Путь к шаблону (по умолчанию: <app>/<model>_list.html)
    context_object_name = 'authors'  # Имя переменной в шаблоне (по умолчанию: object_list)
    paginate_by = 10  # Количество объектов на одной странице (включает пагинацию)
    ordering = ['last_name']  # Сортировка (переопределяет Meta.ordering модели)

    # def get_queryset(self): — позволяет кастомизировать выборку объектов
    #     return Author.objects.filter(first_name__startswith='A')  # Пример фильтрации


    # def get_context_data(self, **kwargs): — добавляет дополнительные данные в контекст шаблона
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Список авторов'
    #     context['total_authors'] = Author.objects.count()
    #     return context


    # Полезен для проверки прав, логирования и т.п.
    # def dispatch(self, request, *args, **kwargs): — вызывается при любом HTTP-запросе (get, post и т.д.)
    #     print(f"Запрос от пользователя: {request.user}")
    #     return super().dispatch(request, *args, **kwargs)


    # def get(self, request, *args, **kwargs): — обрабатывает GET-запрос
    #     print("GET запрос получен")
    #     return super().get(request, *args, **kwargs)


# === 2. AuthorDetailView — Просмотр деталей автора ===
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author_detail.html'
    context_object_name = 'author'  # По умолчанию: object
    slug_field = 'last_name'  # Поле, по которому ищется объект (если используем slug)
    slug_url_kwarg = 'last_name'  # Имя параметра в URL (например, /author/Иванов/)

    # Метод get_object — позволяет изменить логику получения объекта
    # def get_object(self, queryset=None):
    #     obj = get_object_or_404(Author, first_name=self.kwargs['first_name'])
    #     return obj

    # Метод get_context_data — добавляет связанные книги автора
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['books'] = self.object.books.all()  # related_name='books'
    #     return context


# === 3. AuthorCreateView — Создание нового автора ===
class AuthorCreateView(CreateView):
    model = Author
    template_name = 'authors/author_form.html'
    fields = ['first_name', 'last_name', 'birth_date']  # Поля формы (или используй form_class = AuthorForm)
    # form_class = AuthorForm  # Альтернатива: кастомная форма
    success_url = reverse_lazy('author-list')  # Куда перейти после успешного сохранения

    # Метод get_form — позволяет изменить форму (например, добавить классы)
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['first_name'].widget.attrs.update({'class': 'form-control'})
    #     return form

    # Метод form_valid — вызывается при валидной форме
    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user  # Добавить пользователя
    #     return super().form_valid(form)

    # Метод form_invalid — вызывается при ошибках в форме
    # def form_invalid(self, form):
    #     print("Форма невалидна:", form.errors)
    #     return super().form_invalid(form)

    # Метод get_initial — задаёт начальные значения полей
    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['birth_date'] = '1990-01-01'
    #     return initial


# === 4. AuthorUpdateView — Редактирование автора ===
class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'authors/author_form.html'
    fields = ['first_name', 'last_name', 'birth_date']
    context_object_name = 'author'

    # success_url задаётся динамически или через get_success_url
    # success_url = reverse_lazy('author-list')

    # Метод get_success_url — позволяет динамически определить URL после сохранения
    # def get_success_url(self):
    #     return reverse_lazy('author-detail', kwargs={'pk': self.object.pk})

    # Метод get_object — можно ограничить доступ (например, только владельцу)
    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     if obj.created_by != self.request.user:
    #         raise PermissionDenied
    #     return obj


# === 5. AuthorDeleteView — Удаление автора ===
class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/author_confirm_delete.html'
    success_url = reverse_lazy('author-list')
    context_object_name = 'author'

    # Метод get — можно показать предупреждение перед удалением
    # def get(self, request, *args, **kwargs):
    #     print("Пользователь зашёл на страницу подтверждения удаления")
    #     return super().get(request, *args, **kwargs)

    # Метод delete — вызывается при POST-запросе (после подтверждения)
    # def delete(self, request, *args, **kwargs):
    #     print(f"Удалён автор: {self.get_object()}")
    #     return super().delete(request, *args, **kwargs)

    # Метод get_context_data — добавить дополнительную информацию
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['book_count'] = self.object.books.count()
    #     return context


# === 6. BookListView — Список книг с фильтрацией по курсу ===
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    # Метод get_queryset — фильтрация по параметру из URL (например, ?year=first)
    # def get_queryset(self):
    #     queryset = Book.objects.all()
    #     year = self.request.GET.get('year')
    #     if year:
    #         queryset = queryset.filter(year=year)
    #     return queryset

    # Метод get_context_data — добавить фильтры в шаблон
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['year_choices'] = Book.YEAR_IN_PUBLICATE
    #     context['selected_year'] = self.request.GET.get('year', '')
    #     return context


# === 7. BookDetailView — Детали книги + автор ===
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    # Метод get_context_data — добавить информацию об авторе
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['author'] = self.object.authors  # ForeignKey
    #     return context


# === 8. BookCreateView — Создание книги с выбором автора ===
class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'publication_date', 'authors', 'year']
    success_url = reverse_lazy('book-list')

    # Метод form_valid — можно добавить логику (например, логирование)
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     print(f"Книга создана: {self.object.title}")
    #     return response


# === 9. BookUpdateView — Обновление книги ===
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'publication_date', 'authors', 'year']

    # Метод get_success_url — перейти к деталям книги
    # def get_success_url(self):
    #     return reverse_lazy('book-detail', kwargs={'pk': self.object.pk})


# === 10. BookDeleteView — Удаление книги ===
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

    # Метод delete — можно выполнить действия перед удалением
    # def delete(self, request, *args, **kwargs):
    #     book = self.get_object()
    #     print(f"Книга удалена: {book.title}")
    #     return super().delete(request, *args, **kwargs)

# === 11. HomePageView — TemplateView для статичной страницы (например, главная) ===
class HomePageView(TemplateView):
    template_name = 'home.html'  # Указываем шаблон

    # Метод get_context_data — добавляем переменные в шаблон
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Добро пожаловать!'
    #     context['total_authors'] = Author.objects.count()
    #     context['total_books'] = Book.objects.count()
    #     return context

    # Метод dispatch — обрабатывает входящий запрос (можно проверить права)
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('login'))
    #     return super().dispatch(request, *args, **kwargs)

    # Метод get — можно добавить логику при GET-запросе
    # def get(self, request, *args, **kwargs):
    #     print("Пользователь открыл главную страницу")
    #     return super().get(request, *args, **kwargs)

#В файле forms.py определяются модели
# === 12. ContactForm — Пример формы для FormView (не привязана к модели) - основа для 13===
from django.core.validators import MinLengthValidator

class ContactForm(forms.Form):
#validators - список дополнительных валидаторов, которые будут использоваться для проверки значения поля.
#В примере указана минимальная длина сообщения - не менее 2 слов
    name = forms.CharField(max_length=100, label='Ваше имя', validators=[MinLengthValidator(2)])#label - имя поля
    email = forms.EmailField(label='Email', required=False)#required - является ли поле обязательным

    message = forms.CharField(widget=forms.Textarea,# ← делаем из CharField многострочное поле
#В HTML будет как <textarea name="content" ...></textarea>
                              label='Сообщение',
                              initial= "Введите ваше сообщение",#initial - сообщение по умолчанию
                              text_help ="Введите не более 100 слов")#text_help -сообщение-подсказка

    # Можно добавить кастомную валидацию
    # def clean_message(self):
    #     message = self.cleaned_data.get('message')
    #     if 'спам' in message.lower():
    #         raise forms.ValidationError("Сообщение содержит запрещённые слова.")
    #     return message


# === 13. ContactFormView — FormView для обработки формы без модели ===
class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-success')  # Куда перейти после успешной отправки

    # Метод get_initial — начальные значения формы
    # def get_initial(self):
    #     initial = super().get_initial()
    #     if self.request.user.is_authenticated:
    #         initial['name'] = self.request.user.get_full_name()
    #         initial['email'] = self.request.user.email
    #     return initial

    # Метод get_form — можно модифицировать форму (например, стили)
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.fields['name'].widget.attrs.update({'class': 'form-control'})
    #     form.fields['email'].widget.attrs.update({'class': 'form-control'})
    #     form.fields['message'].widget.attrs.update({'class': 'form-control', 'rows': 5})
    #     return form

    # Метод form_valid — вызывается, если форма валидна
    # def form_valid(self, form):
    #     # Здесь можно отправить email, сохранить в файл, лог и т.п.
    #     print("Форма валидна:")
    #     print("Имя:", form.cleaned_data['name'])
    #     print("Email:", form.cleaned_data['email'])
    #     print("Сообщение:", form.cleaned_data['message'])
    #     return super().form_valid(form)

    # Метод form_invalid — вызывается при ошибках ввода
    # def form_invalid(self, form):
    #     print("Форма невалидна. Ошибки:", form.errors)
    #     return super().form_invalid(form)

    # Метод get_context_data — добавить данные в шаблон
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page_title'] = 'Свяжитесь с нами'
    #     return context


# === 14. ContactSuccessView — Просто подтверждение отправки (TemplateView) ===
class ContactSuccessView(TemplateView):
    template_name = 'contact_success.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['message'] = 'Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.'
    #     return context


# === 15. RedirectToHomeView — RedirectView для перенаправления ===
class RedirectToHomeView(RedirectView):
    pattern_name = 'home'  # Перенаправление по имени URL (например, HomePageView)
    # Или можно использовать: url = '/' — прямой URL

    permanent = False  # True — 301 редирект, False — 302 (временный)
    query_string = True  # Передавать ли GET-параметры (например, ?ref=123)

    # Метод get_redirect_url — позволяет динамически определить URL
    # def get_redirect_url(self, *args, **kwargs):
    #     # Пример: перенаправить на профиль пользователя
    #     if self.request.user.is_authenticated:
    #         return reverse('profile', kwargs={'pk': self.request.user.pk})
    #     return reverse('home')

    # Метод dispatch — можно проверить условия перед редиректом
    # def dispatch(self, request, *args, **kwargs):
    #     print(f"Перенаправление запрошено пользователем: {request.user}")
    #     return super().dispatch(request, *args, **kwargs)

    # Метод get — можно добавить логику (например, аналитику)
    # def get(self, request, *args, **kwargs):
    #     response = super().get(request, *args, **kwargs)
    #     # Можно записать лог или событие
    #     return response

# === 16. AuthorCreateWithFormView — CreateView с ModelForm ===
class AuthorCreateWithFormView(CreateView):
    model = Author
    form_class = AuthorForm  # Указываем кастомную ModelForm
    template_name = 'authors/author_form.html'  # Шаблон
    success_url = reverse_lazy('author-list')  # Куда перейти после сохранения

    # Метод get_context_data — добавляем заголовок
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Создать нового автора'
    #     return context

    # Метод form_valid — вызывается при валидной форме
    # def form_valid(self, form):
    #     # Можно добавить действия перед сохранением
    #     print(f"Создаём автора: {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}")
    #     return super().form_valid(form)

    # Метод form_invalid — при ошибках
    # def form_invalid(self, form):
    #     print("Форма содержит ошибки:", form.errors)
    #     return super().form_invalid(form)


# === 17. AuthorUpdateWithFormView — UpdateView с ModelForm ===
class AuthorUpdateWithFormView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authors/author_form.html'
    context_object_name = 'author'

    # Метод get_success_url — динамическое перенаправление
    # def get_success_url(self):
    #     return reverse_lazy('author-detail', kwargs={'pk': self.object.pk})

    # Метод get_object — можно ограничить доступ
    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset)
    #     if obj.birth_date.year < 1900:
    #         raise PermissionDenied("Нельзя редактировать старых авторов.")
    #     return obj


# === 18. BookCreateWithFormView — Создание книги с ModelForm ===
class BookCreateWithFormView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')

    # Метод form_valid — можно модифицировать объект перед сохранением
    # def form_valid(self, form):
    #     # Например, пометим, кто добавил книгу (если есть пользователь)
    #     # form.instance.added_by = self.request.user
    #     return super().form_valid(form)

#============================================ URLS ==================================================
from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),

    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('', views.HomePageView.as_view(), name='home'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('contact/success/', views.ContactSuccessView.as_view(), name='contact-success'),
    path('go-home/', views.RedirectToHomeView.as_view(), name='go-home'),
]
