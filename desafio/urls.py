from django.urls import path
from .views import dioses_romanos, una_vista, dioses_griegos, crear_dios, listado_dioses, acerca_de_mi, eliminar_dios, editar_dios , mostrar_dios 

urlpatterns = [
    path('', una_vista),
    path('dioses_griegos/', dioses_griegos),
    path('dioses_romanos/', dioses_romanos),
    path('crear_dios/', crear_dios, name="crear_dios"),
    path('eliminar_dios/<int:id>/', eliminar_dios, name="eliminar_dios"),
    path('editar_dios/<int:id>/', editar_dios, name="editar_dios"),
    path('listado_dioses/', listado_dioses, name="listado_dioses"),
    path('mostrar_dios/<int:id>/', mostrar_dios, name="mostrar_dios"),
    path('acerca_de_mi/', acerca_de_mi),
]