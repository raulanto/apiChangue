from django.forms import *
from blog.models.Ejercicio import Ejercicio

from django.forms import Textarea


class EjercicioForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['placeholder'] = form.field.label
            form.field.widget.attrs['autocomplete'] = 'off'
        # Para iniciar el primer elemento
        self.fields['nombre'].widget.attrs['autoFocus'] = True

    class Meta:
        model = Ejercicio
        fields = '__all__'

        widgets = {
            'descripcion': Textarea(attrs={
                'cols': 25,
                'rows': 2,
            }),
        }
