from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect

from .models import Adj
from .forms import make_adj_page

def adj_add(request):
    try: request.COOKIES["email"]
    except KeyError: return HttpResponsePermanentRedirect("/auth")
    
    if request.method == "POST":
        form = make_adj_page(request.POST, request.FILES)
        if form.is_valid():
            if not (form.cleaned_data['title'] and form.cleaned_data['text']):
                form.add_error('title', 'Название и текст не могут быть пустыми')
                return HttpResponse("Incorrect answers")
            
            if Adj.objects.filter(title=form.cleaned_data['title']).exists():
                form.add_error('title', 'Форт с таким названием уже существует')
                return HttpResponse("this fort exists")
            
            fort = Adj(
                title=form.cleaned_data['title'],
                link=form.cleaned_data['link'], 
                text=form.cleaned_data['text'],
            )            
            if 'image' in request.FILES:
                fort.image = request.FILES.get("image")
            
            fort.save()
            return HttpResponsePermanentRedirect('/fort')
        
    return render(request, "make.html", {
        "name": "", 
        "type": "рекламы",
        "form": make_adj_page(), 
        "cookie": "email" in request.COOKIES
    })

def about(request):
    try: request.COOKIES["email"]
    except KeyError: return HttpResponsePermanentRedirect("/auth")
    
    return render(request, "about.html", {"cookie": "email" in request.COOKIES})

def to_main(request):
    return HttpResponsePermanentRedirect("/fort")

def custom_404(request):
    return render(request, '404.html', status=404)

def invalid_data(request, back):
    return render(request, 'invalid_data.html', {"back": back})
