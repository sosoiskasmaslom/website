from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseNotFound
  
from .forms import regist_page, auth_page
from .models import User
from .encrypt import fast_hash, check, encrypt, decrypt

def registration(request):
    if request.method == "POST":
        data = regist_page(request.POST)
        if data.is_valid():
            try:
                user = User.objects.get(email=data.cleaned_data["email"])
            except User.DoesNotExist: pass
            else: return HttpResponse("User with this email is in db")

            user = User()

            user.first_name = (data.cleaned_data["first_name"])
            user.last_name = (data.cleaned_data["last_name"])
            user.patronymic =(data.cleaned_data["patronymic"])
            user.email = (data.cleaned_data["email"])
            user.password = fast_hash(data.cleaned_data["password"])
            user.birth_date = data.cleaned_data["birth_date"]

            user.save()
            
            response = HttpResponsePermanentRedirect("/fort")
            response.set_cookie("email", data.cleaned_data["email"], path="/")
            return response
        else: 
            return HttpResponsePermanentRedirect("/reg/invalid_data")
    else: return render(request, "auth.html", {"title": "Зарегистрироваться", "form": regist_page()})

def auth(request, err = False):
    if request.method == "POST":
        data = auth_page(request.POST)
        if data.is_valid():
            try:
                user = User.objects.get(email=(data.cleaned_data["email"]))
            except User.DoesNotExist:
                return HttpResponsePermanentRedirect("/auth/err")
            except models.MultipleObjectsReturned:
                return HttpResponseNotFound("Users too much")
            
            if check(data.cleaned_data["password"], user.password):
                response = HttpResponsePermanentRedirect('/fort')
                response.set_cookie("email", data.cleaned_data["email"], path="/")
                return response
            else: return HttpResponsePermanentRedirect("/auth/err")
        else: return HttpResponsePermanentRedirect("/auth/invalid_data")
    else: return render(request, "auth.html", {"title": "Войти", "form": auth_page, "err": err})

def authr(request):
    return auth(request, True)

def profile(request, email=None):
    if request.method == "POST":
        if request.POST.get("action") == "exit":
            response = HttpResponsePermanentRedirect('/fort')
            response.delete_cookie("email")
            return response
        if request.POST.get("action") == "main": return HttpResponsePermanentRedirect("/fort")
    if email is None: 
        try:
            email = request.COOKIES["email"]
        except KeyError:
            return HttpResponseNotFound("<h1>Page not found</h1>")
    try:
        user = User.objects.get(email=(email))
    except User.DoesNotExist: 
        return HttpResponseNotFound("<h1>User not found</h1>")
    data = [
        ["Имя", (user.first_name)],
        ["Фамилия", (user.last_name)],
        ["Отчество", (user.patronymic) if user.patronymic else "*отсутствует*"],
        ["Почта", (user.email)],
        ["Дата рождения", user.birth_date],
    ]
    return render(request, "profile.html", {"data": data})
