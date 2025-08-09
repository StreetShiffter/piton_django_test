from .models import Author, Book
from django import forms

# === ModelForm для Author ===
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author  # Указываем, к какой модели привязана форма
        fields = ['first_name', 'last_name', 'birth_date']  # Поля, которые будут в форме
        # exclude = ['some_field']  # Или можно исключить поля (вместо fields)

        # Настройка полей (подпись, виджеты и т.п.)
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'  # HTML5 date picker
            }),
        }

        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'birth_date': 'Дата рождения',
        }

    # Кастомная валидация: проверим, что дата рождения не в будущем
    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        from django.utils import timezone
        if birth_date and birth_date > timezone.now().date():
            raise forms.ValidationError("Дата рождения не может быть в будущем.")
        return birth_date

    # Кастомная валидация всей формы (если нужно проверить несколько полей)
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        # Пример: запрещаем создавать автора с пустыми именем и фамилией
        if not first_name and not last_name:
            raise forms.ValidationError("Имя и фамилия не могут быть пустыми одновременно.")

        # Пример: нельзя, чтобы имя и фамилия совпадали
        if first_name and last_name and first_name.lower() == last_name.lower():
            self.add_error('last_name', "Фамилия не может совпадать с именем.")

        return cleaned_data


# === ModelForm для Book ===
class BookForm(forms.ModelForm):
    class Meta:
        model = Book #ссылка на модель, на основе которой будет создана форма.
        fields = ['title', 'publication_date', 'authors', 'year']#список полей модели, которые будут включены в форму.
        #exclude = ['authors'] -  список полей модели, которые не будут включены в форму.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'authors': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
        }

    # Добавим проверку: дата публикации не может быть позже сегодня
    def clean_publication_date(self):
        pub_date = self.cleaned_data.get('publication_date')
        from django.utils import timezone
        if pub_date and pub_date > timezone.now().date():
            raise forms.ValidationError("Дата публикации не может быть в будущем.")
        return pub_date

    # Можно фильтровать выбор авторов (например, только живые, или по алфавиту)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Сортируем авторов по фамилии
        self.fields['authors'].queryset = Author.objects.all().order_by('last_name')
        # Пример: фильтр по возрасту (авторы старше 18)
        # self.fields['authors'].queryset = Author.objects.filter(birth_date__lte=some_date)