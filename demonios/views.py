from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BusquedaDemonios
from .models import CrearDemonio

class ListadoDemonios(ListView):
    model=CrearDemonio
    template_name = "demonios/listado_demonios.html"

    def get_queryset(self):
        nombre = self.request.GET.get("nombre", "")
        if nombre:
            object_list = self.model.objects.filter(nombre__icontains=nombre)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaDemonios()
        return context    
    
    
    
class CrearDemonio2(CreateView):
    model=CrearDemonio
    template_name = "demonios/crear_demonio.html"
    success_url = "/demonios/listado_demonios"
    fields = ["nombre", "simbolo", "origen", "reseña", "fecha_creacion", "autor"]    
    
    
class EditarDemonio(LoginRequiredMixin,UpdateView):
    model=CrearDemonio
    template_name = "demonios/editar_demonio.html"
    success_url = "/demonios/listado_demonios"
    fields = ["nombre", "simbolo", "origen", "reseña", "fecha_creacion", "autor"]    
    
    
class EliminarDemonio(DeleteView, LoginRequiredMixin):
    model=CrearDemonio
    template_name = "demonios/eliminar_demonio.html"
    success_url = "/demonios/listado_demonios"  
    
    
class MostrarDemonio(DetailView):
    model=CrearDemonio
    template_name = "demonios/mostrar_demonio.html"