from django.urls import path
from .views import una_vista, un_template

urlpatterns = [
    path('', una_vista),
    path('mi_template/', un_template),
]