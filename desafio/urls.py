from django.urls import path
from .views import una_vista, dioses_griegos

urlpatterns = [
    path('', una_vista),
    path('dioses_griegos/', dioses_griegos),
]