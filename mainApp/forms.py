from dataclasses import field
from django import forms
from mainApp.models import Docente
class formBloqueDias(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
