"""Requerimiento Forms"""

# Django
from django import forms
# sgo Model
from utils.models import Cliente, Negocio
from requerimientos.models import Requerimiento


class RequerimientoCreateForm(forms.ModelForm):
    nombre = forms.CharField(required=True, label="Nombre",
                                 widget=forms.TextInput(attrs={'class': "form-control-lg"}))
    comentario = forms.CharField(required=True, label="Comentario",
                                widget=forms.Textarea(attrs={'class': "form-control-lg"}))

    # clientes = forms.ModelMultipleChoiceField(queryset=Cliente.objects.none(), required=True, label="Cliente",
    #                                         widget=forms.SelectMultiple(
    #                                             attrs={'class': 'selectpicker show-tick',
    #                                                    'data-size': '5',
    #                                                    'data-live-search': 'true',
    #                                                    'data-live-search-normalize': 'true'
    #                                                    })
    #                                         )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        print(user)
        super(RequerimientoCreateForm, self).__init__(*args, **kwargs)
        if not user.groups.filter(name='Administrador').exists():
            self.fields['clientes'].queryset = Cliente.objects.filter(id__in=user.cliente.all())
        else:
            self.fields['clientes'].queryset = Cliente.objects.all()

    class Meta:
        model = Requerimiento
        fields = ("nombre", "centro_costo", "comentario", "planta", "status", )
