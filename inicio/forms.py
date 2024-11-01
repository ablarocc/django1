from django import forms

class CrearVestidoForm(forms.Form):
    color = forms.CharField(max_length=20)
    escote = forms.CharField(max_length=25)
    mangas = forms.CharField(max_length=15)
    
class BuscarModeloForm(forms.Form):
    color = forms.CharField(max_length=20 , required=False)
    escote = forms.CharField(max_length=25, required= False)
    