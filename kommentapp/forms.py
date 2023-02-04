from django import forms
from .models import KommentModel

class KommentForm(forms.ModelForm):
    exclude = ("date", )
    
    class Meta:
        model = KommentModel
        
    