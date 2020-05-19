from django import forms
from django.forms import DateInput

from .models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        exclude = ('usuario', )
        fields = '__all__'
        # widgets = {
        #     'data_expiracao': DateInput(attrs={'type': 'date'}),
        # }