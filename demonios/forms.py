from django import forms

class BusquedaDemonios(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)