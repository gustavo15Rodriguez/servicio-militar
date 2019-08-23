from apps.soldado.models import Servicio,Soldado,Cuerpo
from django import forms


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio

        fields = "__all__"

        labels = {
            'id_servicio': 'ID del servicio',
            'descripcion': 'Descripcion',
        }

        widgets = {
            'id_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SoldadoForm(forms.ModelForm):
    class Meta:
        model = Soldado

        fields = "__all__"


        labels = {
            'nombre':'Nombre',
            'apellido':'Apellido',
            'grado':'Grado',
            'servicio':'Servicio',
            'cuerpo':'Cuerpo',
            'compania':'Compania',
        }

    def __init__(self, *args, **kwargs):
        super(SoldadoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



class CuerpoForm(forms.ModelForm):
    class Meta:
        model = Cuerpo

        fields = "__all__"

        labels = {
            'id_cuerpo': 'ID del cuerpo',
            'denominacion': 'Denominacion',
        }

        widgets = {
            'id_cuerpo': forms.TextInput(attrs={'class': 'form-control'}),
            'denominacion': forms.TextInput(attrs={'class': 'form-control'}),
        }