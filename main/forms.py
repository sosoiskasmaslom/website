
from django import forms

class make_adj_page(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Название рекламы",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Это поле обязательно для заполнения',
        }
    )
    link = forms.CharField(
        max_length=100,
        label="Ссылка",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'Это поле обязательно для заполнения',
        }
    )
    image = forms.ImageField(
        label="Изображение рекламы",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        required=False
    )
    text = forms.CharField(
        label="Текст рекламы",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        required=False,
        error_messages={
            'required': 'Это поле обязательно для заполнения'
        }
    )