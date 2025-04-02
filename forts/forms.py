from django import forms
from django.core.exceptions import ValidationError

class make_excursion_page(forms.Form):
    meet_place = forms.CharField(
        label="Место встречи",
        max_length=100
    )
    time = forms.DateTimeField(label="Время встречи")
    count = forms.IntegerField(label="Количество мест", min_value=1)

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

    # def __init__(self, *args, **kwargs):
    #     dynamic_required = kwargs.pop('dynamic_required', True) 
    #     super().__init__(*args, **kwargs)

    #     self.fields['title'].required = dynamic_required
    #     # self.fields['image'].required = dynamic_required
    #     self.fields['text'].required = dynamic_required