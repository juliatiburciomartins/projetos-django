
from django.contrib import admin
from django.urls import path
from projeexemplo1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sobre, name ='sobre'),
    path('autor/', views.autor, name ='autor'),
    path('noticias/', views.noticias, name ='lala'),
    path('empresas/', views.empresas, name ='empresas')
]
