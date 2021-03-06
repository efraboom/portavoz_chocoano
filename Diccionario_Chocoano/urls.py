"""Diccionario_Chocoano URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from portavoz.views import ErrorView,Error505View 
from django.conf.urls import handler404,handler500
from portavoz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    #path('resultados', views.Resultados.as_view(), name='resultados'),
    path('resultados', views.resultados, name='resultados'),
    path('acerca-de', views.acerca_de, name='info'),
    path('afro', views.afro, name='afro'),
    path('indigena', views.indigena, name='indigena'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 =  ErrorView.as_view()
handler500 = Error505View.as_error_view()
