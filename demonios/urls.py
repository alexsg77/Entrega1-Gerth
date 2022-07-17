from django.urls import path
from . import  views

urlpatterns = [
    path('listado_demonios/', views.ListadoDemonios.as_view(), name="listado_demonios"),
    path('crear_demonio', views.CrearDemonio2.as_view(), name="crear_demonio"),
    path('editar_demonio/<int:pk>/', views.EditarDemonio.as_view(), name="editar_demonio"),
    path('eliminar_demonio/<int:pk>/', views.EliminarDemonio.as_view(), name="eliminar_demonio"),
    path('mostrar_demonio/<int:pk>/', views.MostrarDemonio.as_view(), name="mostrar_demonio"),
    
]