from django import forms

class regist_page(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField(required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=8)
    birth_date = forms.DateField()

class auth_page(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8)