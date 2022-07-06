from django import forms

class FormDios(forms.Form):
    nombre = forms.CharField(max_length=30)
    simbolo = forms.CharField(max_length=30)
    origen = forms.CharField(max_length=30)
    reseña = forms.CharField(max_length=3000)
    
class BusquedaDioses(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)