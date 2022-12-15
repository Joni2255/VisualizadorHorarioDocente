from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def bloque(request):
    return render(request, 'asignarbloque.html')
