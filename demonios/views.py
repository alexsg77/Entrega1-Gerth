from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from .models import CrearDemonio

class ListadoDemonios(ListView):
    model=CrearDemonio
    template_name = "demonios/listado_demonios.html"
    
    
class CrearDemonio2(CreateView):
    model=CrearDemonio
    template_name = "demonios/crear_demonio.html"
    success_url = "/demonios/listado_demonios"
    fields = ["nombre", "simbolo", "origen", "reseña"]    
    
    
class EditarDemonio(UpdateView):
    model=CrearDemonio
    template_name = "demonios/editar_demonio.html"
    success_url = "/demonios/listado_demonios"
    fields = ["nombre", "simbolo", "origen", "reseña"]    
    
    
class EliminarDemonio(DeleteView):
    model=CrearDemonio
    template_name = "demonios/eliminar_demonio.html"
    success_url = "/demonios/listado_demonios"  
    
    
class MostrarDemonio(DetailView):
    model=CrearDemonio
    template_name = "demonios/mostrar_demonio.html"