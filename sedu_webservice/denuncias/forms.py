from django import forms
from .models import Reclamacao

class ReclamacaoForm(forms.ModelForm):
    
    class Meta:
        model = Reclamacao
        fields = '__all__'
