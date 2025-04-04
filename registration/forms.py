from django import forms

class regist_page(forms.Form):
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}),
        error_messages={
            "required": "Введите своё имя",
        },
    )
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}),
        error_messages={
            "required": "Введите свою фамилию",
        },
    )
    patronymic = forms.CharField(
        label="Отчество",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Введите отчество'}),
    )
    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.TextInput(attrs={'placeholder': 'Формат example@mail.com'}),
        error_messages={
            "required": "Введите свою почту",
            "invalid": "Некорректная почта",
        },
    )
    password = forms.CharField(
        label="Пароль",
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль от 8 символов'}),
        error_messages={
            "required": "Введите пароль",
            "min_length": "Пароль должен содержать не менее 8 символов",
        },
    )
    birth_date = forms.DateField(
        label="Дата рождения",
        widget=forms.DateInput(attrs={'placeholder': 'Формат гггг.мм.дд'}),
        error_messages={
            "required": "Введите дату рождения",
            "invalid": "Некорректная дата",
        },
    )

class auth_page(forms.Form):
    email = forms.EmailField(
        label="Почта",
        widget=forms.TextInput(attrs={'placeholder': 'Формат example@mail.com'}),
        error_messages={
            "required": "Введите свою почту",
            "invalid": "Некорректная почта",
        },
    )
    password = forms.CharField(
        min_length=8,
        label="Пароль",
        widget=forms.TextInput(attrs={'placeholder': 'Пароль от 8 символов'}),
        error_messages={
            "required": "Введите пароль",
            "invalid": "Некорректный пароль",
        },
    )
