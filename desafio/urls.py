from django.urls import path
from .views import dioses_romanos, una_vista, dioses_griegos, crear_dios, listado_dioses, acerca_de_mi  

urlpatterns = [
    path('', una_vista),
    path('dioses_griegos/', dioses_griegos),
    path('dioses_romanos/', dioses_romanos),
    path('crear_dios/', crear_dios, name="crear_dios"),
    path('listado_dioses/', listado_dioses, name="listado_dioses"),
    path('acerca_de_mi/', acerca_de_mi),
]