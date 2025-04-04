from django import forms
from django.core.exceptions import ValidationError

class make_excursion_page(forms.Form):
    meet_place = forms.CharField(
        label="Место встречи",
        widget=forms.TextInput(attrs={'placeholder': 'Введите место встречи'}),
        error_messages={
            "required": "Введите название экскурсии",
        },
    )
    time = forms.DateTimeField(
        label="Дата проведения",
        widget=forms.DateInput(attrs={'placeholder': 'Формат гггг.мм.дд чч:мм'}),
        error_messages={
            "required": "Введите дату проведения экскурсии",
            "invalid": "Некорректная дата",
        },
    )
    count = forms.IntegerField(
        label="Максимальное количество участников",
        widget=forms.NumberInput(attrs={'placeholder': 'Введите число участников'}),
        error_messages={
            "required": "Введите максимальное количество участников",
            "invalid": "Некорректное число",
        },
    )
    
class make_fort_page(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Название форта",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
        error_messages={
            'required': 'Это поле обязательно для заполнения',
            'max_length': 'Слишком длинное название форта'
        }
    )
    image = forms.ImageField(
        label="Изображение форта",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        required=False
    )
    text = forms.CharField(
        label="Описание",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        required=False,
        error_messages={
            'required': 'Это поле обязательно для заполнения'
        }
    )

class search(forms.Form):
    search = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Поиск по фортам...'}),
        required=False,
        error_messages={
            'required': 'Это поле обязательно для заполнения',
            'max_length': 'Слишком длинный запрос'
        }
    )