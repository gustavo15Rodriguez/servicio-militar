from apps.cuartel.models import Compania,Cuartel
from django import forms


class CompaniaForm(forms.ModelForm):
    class Meta:
        model = Compania

        fields = "__all__"

        labels = {
            'id_compania': 'ID de la compañia',
            'actividad': 'Actividad',
        }

        widgets = {
            'id_compania': forms.TextInput(attrs={'class':'form-control'}),
            'actividad': forms.TextInput(attrs={'class':'form-control'}),
        }



class CuartelForm(forms.ModelForm):
    class Meta:
        model = Cuartel

        fields = [
            'nombre',
            'direccion',
        ]

        labels = {
            'nombre': 'Nombre',
            'direccion': 'Direccion',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }