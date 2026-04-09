from django.http import HttpResponse

def sobre(request):
    return HttpResponse('Rota Sobre')

def autor(request):
    return HttpResponse('Rota Autor')

def noticias(request):
    return HttpResponse('Rota Noticias')

def empresas(request):
    return HttpResponse('Rota Empresas')