from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from desafio.models import Prueba

# Create your views here.
def una_vista(request):
    return render(request, "index.html")

def dioses_griegos(request):
    # template = loader.get_template("index.html")
    
    dios1 = Prueba(nombre="Zeus", simbolo = "Cielo", origen = "Griego")
    dios2 = Prueba(nombre="Poseidón", simbolo = "Mar", origen = "Griego")
    dios3 = Prueba(nombre="Ares", simbolo = "Guerra", origen = "Griego")
    # dios1.save()
    # dios2.save()
    # dios3.save()
    
    # render = template.render({"lista_objetos": [dios1, dios2, dios3]})
    # return HttpResponse(render)
    return render(request, "dioses_griegos.html", {"lista_objetos": [dios1, dios2, dios3]})