"""
URL configuration for coolsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

from main import views as main
from forts import views as forts
from registration import views as reg

urlpatterns = [
    path('<back>/invalid_data', main.invalid_data),
    path('profile/<str:email>', reg.profile),
    path('auth/err', reg.authr),   
    re_path('^profile', reg.profile),
    re_path('^auth', reg.auth),
    re_path('^reg', reg.registration),

    path('excursion/<name>', forts.excursion),
    path('excursion/<name>/make', forts.excursion_make),
    path('excursion/edit/<name>/<id>', forts.excursion_edit),
    path('excursion/delete/<name>/<id>', forts.excursion_delete),
    re_path('excursion', forts.excursion),

    path('fort/edit/<id>', forts.fort_edit),
    path('fort/delete/<id>', forts.fort_delete),
    re_path('fort/add', forts.fort_add),
    re_path('search', forts.fort),
    re_path('fort', forts.fort),

    path('admin/', admin.site.urls),
    path('adj_add', main.adj_add),
    re_path('^about', main.about),

    re_path('', main.custom_404),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)