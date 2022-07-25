from email.policy import default
from django import forms
from ckeditor.fields import RichTextFormField

class FormDios(forms.Form):
    nombre = forms.CharField(max_length=30)
    simbolo = forms.CharField(max_length=30)
    origen = forms.CharField(max_length=30)
    reseña = RichTextFormField()
    fecha_creacion = forms.DateField(required=False)
    autor = forms.CharField(required=False, max_length=30)
    
class BusquedaDioses(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)