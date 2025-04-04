from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect

from .models import Fort, Excursion
from main.models import Adj
from .forms import make_excursion_page, make_fort_page, search

import os
from random import choice

def fort(request):

    if request.method == "POST":
        search_text = request.POST.get("search", "")
        if search_text:
            forts = Fort.objects.filter(title__icontains=search_text)
            data = [
                {
                    "id": fort.id,
                    "title": fort.title,
                    "image": '/'.join(fort.image.url.split('/')[2:]) if fort.image else None,
                    "text": fort.text,
                }
                for fort in forts
            ]
            return render(request, "forts.html", {
                "search": search(),
                "forts": data,
                "cookie": "email" in request.COOKIES
            })

    data = [
        {
            "id": fort.id,
            "title": fort.title,
            # какой же блять пиздец это
            # это сука не строка, это блядская хуета, сука
            # это не должно работать, ахуевшая ты тварь
            "image": '/'.join(fort.image.url.split('/')[2:]) if fort.image else None,
            "text": fort.text,
        }
        for fort in Fort.objects.all()
    ]
    adj_data = [
            {
            "title": adj.title,
            "link": adj.link,
            "image": '/'.join(adj.image.url.split('/')[2:]) if adj.image else None,
            "text": adj.text,
        } for adj in Adj.objects.all()
    ]

    return render(request, "forts.html", {
        "search": search(),
        "forts": data,
        "adjs": adj_data,
        "cookie": "email" in request.COOKIES
    })

def fort_add(request):
    try: request.COOKIES["email"]
    except KeyError: return HttpResponsePermanentRedirect("/auth")
    
    if request.method == "POST":
        form = make_fort_page(request.POST, request.FILES)
        form.fields['title'].required = True
        form.fields['text'].required = True
        if form.is_valid():
            if not (form.cleaned_data['title'] and form.cleaned_data['text']):
                form.add_error('title', 'Название и текст не могут быть пустыми')
                return HttpResponse("Incorrect answers")
            
            if Fort.objects.filter(title=form.cleaned_data['title']).exists():
                form.add_error('title', 'Форт с таким названием уже существует')
                return HttpResponse("this fort exists")
            
            fort = Fort(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text']
            )            
            if 'image' in request.FILES:
                fort.image = request.FILES.get("image")
            
            fort.save()
            return HttpResponsePermanentRedirect('/fort')
        
    return render(request, "make.html", {
        "name": "", 
        "type": "форта",
        "form": make_fort_page(), 
        "cookie": "email" in request.COOKIES
    })

def fort_edit(request, id):
    try: request.COOKIES["email"]
    except KeyError: return HttpResponsePermanentRedirect("/auth")
    
    fort = Fort.objects.get(id=id)
    if request.method == "POST":
        form = make_fort_page(request.POST, request.FILES)
        if form.is_valid():
            fort.title = form.cleaned_data['title'] if form.cleaned_data['title'] else fort.title
            fort.text = form.cleaned_data['text'] if form.cleaned_data['text'] else fort.text
            fort.image = request.FILES.get("image") if request.FILES.get("image") else fort.image
            
            fort.save()
            return HttpResponsePermanentRedirect('/fort')
        else: return HttpResponse("Incorrect answers")

    return render(request, "make.html", {
        "name": "", 
        "type": "форта",
        "form": make_fort_page(), 
        "cookie": "email" in request.COOKIES
    })

def fort_delete(request, id):
    try: request.COOKIES["email"]
    except KeyError: return HttpResponsePermanentRedirect("/auth")
    
    fort = Fort.objects.get(id=id)
    Excursion.objects.filter(title=fort.title).delete()

    try: os.remove(fort.image.path)
    except FileNotFoundError: pass
    
    fort.delete()
    return HttpResponsePermanentRedirect("/fort")

def excursion(request, name=None):
    try: request.COOKIES["email"]
    except KeyError: return HttpResponsePermanentRedirect("/auth")
    
    if name is None: 
        data = {}
        for title in set([exc.title for exc in Excursion.objects.all()]):
            data[title] = [
                { "id": exc.id, "meet_place": exc.meet_place, "time": exc.time, "count": exc.count }
                for exc in Excursion.objects.filter(title=title)
            ]

    else:
        data = {name: [
                { "id": exc.id, "meet_place": exc.meet_place, "time": exc.time, "count": exc.count }
                for exc in Excursion.objects.filter(title=name)
            ]}

    return render(request, "excursions.html", {
        "name": name is not None,
        "data": data, 
        "cookie": "email" in request.COOKIES
    })

def excursion_make(request, name):
    try: request.COOKIES["email"]
    except KeyError: return HttpResponsePermanentRedirect("/auth")
    
    if request.method == "POST":
        data = make_excursion_page(request.POST)
        if data.is_valid():
            try: 
                excursion = Excursion.objects.get(
                    title=name,
                    time=data.cleaned_data["time"]
                )
            except Excursion.DoesNotExist: pass
            else: return HttpResponse("Excursion exists at this time")
    
            excursion = Excursion(
                title = name,
                meet_place = data.cleaned_data["meet_place"],
                time = data.cleaned_data["time"],
                count = data.cleaned_data["count"],
            )

            excursion.save()
            return HttpResponsePermanentRedirect("/excursion")
        else: return HttpResponse("Incorrect answers")

    return render(request, "make.html", {
        "name": name, 
        "type": "экскурсии",
        "form": make_excursion_page(), 
        "cookie": "email" in request.COOKIES
    })

def excursion_edit(request, name, id):
    try: request.COOKIES["email"]
    except KeyError: return HttpResponsePermanentRedirect("/auth")
    
    if request.method == "POST":
        return excursion_make(request, name)
    
    excursion_delete(request, name, id)
    return excursion_make(request, name)

def excursion_delete(request, name, id=None):
    try: request.COOKIES["email"]
    except KeyError: return HttpResponsePermanentRedirect("/auth")
    
    try:
        Excursion.objects.get(
            id=id,
            title=name 
        ).delete()
    except Excursion.DoesNotExist:
        if id is None: return HttpResponse("Error")
    return HttpResponsePermanentRedirect("/excursion")
