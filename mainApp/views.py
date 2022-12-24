from django.shortcuts import render
from mainApp.models import Bloques, Docente, Dias, Bloque_dias
from mainApp.forms import formBloqueDias
from django.db.models import Q

def index(req):
    bloques = Bloques.objects.all()
    docente = Docente.objects.all().order_by('orden_dia')
    dias = Dias.objects.all()
    bloque_dias = Bloque_dias.objects.all().order_by('dia')
    data = {
        "bloques" : bloques,
        "docente" : docente,
        "dias" : dias,
        "bloque_dias" : bloque_dias,
    }
    return render(req, 'index.html', data)

def search(request):
    template_name = "index.html"
    busqueda = request.GET["busebump"]
    docente = Docente.objects.filter(nombre__icontains=busqueda)
    context = {'docente' : docente, }

    return render(request, template_name ,context)

def bloque(request):
    form = formBloqueDias()

    if request.method == 'POST':
        form = formBloqueDias(request.POST)
        if form.is_valid():
            form.save()
            return index(request)

    data = {'form': form}
    return render(request, 'asignarbloque.html', data)