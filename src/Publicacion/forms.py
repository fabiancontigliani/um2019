from django import forms
from django.utils.html import strip_tags

from .models import Publicacion

class PublicacionForm(forms.ModelForm):
  body = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Publicacion', 'class': 'form-control'}))
 
  class Meta:
    model = Publicacion
    exclude = ('user',)
