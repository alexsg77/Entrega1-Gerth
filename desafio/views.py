from django.shortcuts import redirect, render
from desafio.forms import BusquedaDioses, FormDios
from desafio.models import DiosGriego, DiosRomano, CrearDios
from django.contrib.auth.decorators import login_required

# Create your views here.
def una_vista(request):
    return render(request, "index.html")

def acerca_de_mi(request):
    return render(request, "about.html")

def dioses_griegos(request):

    
    dios1 = DiosGriego(nombre="Zeus", simbolo = "Cielo", origen = "Griego")
    dios2 = DiosGriego(nombre="Poseidón", simbolo = "Mar", origen = "Griego")
    dios3 = DiosGriego(nombre="Ares", simbolo = "Guerra", origen = "Griego")
    dios4 = DiosGriego(nombre="Afrodita", simbolo = "Amor", origen = "Griego")
    dios5 = DiosGriego(nombre="Hera", simbolo = "Mujeres", origen = "Griego")
    dios6 = DiosGriego(nombre="Demeter", simbolo = "Cosecha", origen = "Griego")
    dios7 = DiosGriego(nombre="Athena", simbolo = "Estrategia", origen = "Griego")
    dios8 = DiosGriego(nombre="Apolo", simbolo = "Sol/Música/Poesia", origen = "Griego")
    dios9 = DiosGriego(nombre="Artemisa", simbolo = "Caza", origen = "Griego")
    dios10 = DiosGriego(nombre="Hefesto", simbolo = "Fuego", origen = "Griego")
    dios11 = DiosGriego(nombre="Hermes", simbolo = "Mensajero", origen = "Griego")
    dios12 = DiosGriego(nombre="Dionisio", simbolo = "Vino", origen = "Griego")

    return render(request, "dioses_griegos.html", {"lista_griegos": [dios1, dios2, dios3, dios4, dios5, dios6, dios7, dios8, dios9, dios10, dios11, dios12]})

def dioses_romanos(request):

    
    dios1 = DiosRomano(nombre="Júpiter", simbolo = "Cielo", origen = "Romano")
    dios2 = DiosRomano(nombre="Neptuno", simbolo = "Mar", origen = "Romano")
    dios3 = DiosRomano(nombre="Marte", simbolo = "Guerra", origen = "Romano")
    dios4 = DiosRomano(nombre="Juno", simbolo = "Reina", origen = "Romano")
    dios5 = DiosRomano(nombre="Saturno", simbolo = "Tiempo", origen = "Romano")
    dios6 = DiosRomano(nombre="Plutón", simbolo = "Inframundo", origen = "Romano")
    dios7 = DiosRomano(nombre="Venus", simbolo = "Amor y Belleza", origen = "Romano")
    dios8 = DiosRomano(nombre="Minerva", simbolo = "Sabiduria", origen = "Romano")
    dios9 = DiosRomano(nombre="Mercurio", simbolo = "Mensajero", origen = "Romano")
    dios10 = DiosRomano(nombre="Apolo", simbolo = "Sol", origen = "Romano")
    dios11 = DiosRomano(nombre="Diana", simbolo = "Caza", origen = "Romano")
    dios12 = DiosRomano(nombre="Ceres", simbolo = "Agricultura y Familia", origen = "Romano")

    return render(request, "dioses_romanos.html", {"lista_romanos": [dios1, dios2, dios3, dios4, dios5, dios6, dios7, dios8, dios9, dios10, dios11, dios12]})

def crear_dios(request):
    
    if request.method == "POST":
        form = FormDios(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            diospropio = CrearDios(nombre=data.get("nombre"), simbolo=data.get("simbolo"), origen=data.get("origen"), reseña=data.get("reseña"), fecha_creacion=data.get("fecha_creacion"), autor=data.get("autor"))
            diospropio.save()
            return redirect("listado_dioses")
        
        else:
            return render(request, "dioses/crear_dios.html", {"form": form})
            
    form_dios = FormDios()

    
    return render(request, "dioses/crear_dios.html", {"form": form_dios})

def listado_dioses(request):
    
    nombre_de_busqueda = request.GET.get("nombre")
    
    if nombre_de_busqueda:
        listado_dioses = CrearDios.objects.filter(nombre__icontains=nombre_de_busqueda)
    else:
        listado_dioses = CrearDios.objects.all()
    form = BusquedaDioses()
    return render(request, "dioses/listado_dioses.html", {"listado_dioses": listado_dioses, "form": form})
    
@login_required    
def editar_dios(request, id):
    diospropio = CrearDios.objects.get(id=id) 
    
    if request.method =="POST":
        form = FormDios(request.POST)
        if form.is_valid():  
            diospropio.nombre = form.cleaned_data.get("nombre")
            diospropio.simbolo = form.cleaned_data.get("simbolo")
            diospropio.origen = form.cleaned_data.get("origen")
            diospropio.reseña = form.cleaned_data.get("reseña")
            diospropio.fecha_creacion = form.cleaned_data.get("fecha_creacion")
            diospropio.autor = form.cleaned_data.get("autor")
            diospropio.save()
            
            return redirect("listado_dioses")
        else:
            return render(request, "dioses/editar_dios.html", {"form": form, "dios": diospropio})
    
    form_diospropio = FormDios(initial={"nombre": diospropio.nombre, "simbolo": diospropio.simbolo, "origen":  diospropio.origen, "reseña": diospropio.reseña, "fecha_creacion": diospropio.fecha_creacion, "autor": diospropio.autor})    
    
    return render(request, "dioses/editar_dios.html", {"form": form_diospropio, "diospropio": diospropio})
    
    
@login_required    
def eliminar_dios(request, id):
    diospropio = CrearDios.objects.get(id=id)
    diospropio.delete()
    return redirect("listado_dioses")

def mostrar_dios(request, id):
    diospropio = CrearDios.objects.get(id=id)
    return render(request, 'dioses/mostrar_dios.html', {'diospropio': diospropio})