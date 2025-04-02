from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from datetime import datetime

from .models import Fort, Excursion
from .forms import make_excursion_page, make_fort_page

def forts(request):

    data = [
        {"id": fort.id, "title": fort.title, "img": fort.image, "text": fort.text}
        for fort in Fort.objects.all()
    ]

    return render(request, "forts.html", {"forts": data, "cookie": "email" in request.COOKIES})

def excursion(request, name=None):

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
    
            excursion = Excursion()
            excursion.title = name
            excursion.meet_place = data.cleaned_data["meet_place"]
            excursion.time = data.cleaned_data["time"]
            excursion.count = data.cleaned_data["count"]

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
    if request.method == "POST":
        return excursion_make(request, name)
    
    excursion_delete(request, name, id)
    return excursion_make(request, name)

def excursion_delete(request, name, id=None):
    try:
        Excursion.objects.get(
            id=id,
            title=name 
        ).delete()
    except Excursion.DoesNotExist:
        if id is None: return HttpResponse("Error")
    return HttpResponsePermanentRedirect("/excursion")

def fort_add(request):
    if request.method == "POST":
        data = make_fort_page(request.POST, request.FILES)
        if data.is_valid():
            try: Excursion.objects.get(title=data.cleaned_data["title"])
            except Excursion.DoesNotExist: pass
            else: return HttpResponse("Fort exists at this time")

            fort = Fort()
            fort.title = data.cleaned_data["title"]
            # fort.image = data.cleaned_data["image"]
            fort.text = data.cleaned_data["text"]

            return HttpResponsePermanentRedirect("/fort")
        else: return HttpResponse("Incorrect answers")

    return render(request, "make.html", {
        "name": None, 
        "type": "форта",
        "form": make_fort_page(), 
        "cookie": "email" in request.COOKIES
    })

def fort_delete(request, id):
    fort = Fort.objects.get(id=id)
    Excursion.objects.filter(title=fort.title).delete()
    fort.delete()
    return HttpResponsePermanentRedirect("/")

def about(request):
    return render(request, "about.html", {"cookie": "email" in request.COOKIES})

def work_with_db():
    # idk where i have to put it
    for i in range(1, 13):
        with open(f"forts/static/texts/fort{i}.txt", 'r') as file:
            all = file.read()
            fort = Fort()

            fort.title = all.split(".")[0]
            fort.text = all[len(fort.title)+2:]
            fort.image = f"static/images/fort{i}.png"

            fort.save()