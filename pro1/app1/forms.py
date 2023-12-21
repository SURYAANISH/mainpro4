from django import forms
from .models import Dress


class DressForm(forms.ModelForm):
    class Meta:
        model = Dress

        fields='__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),

        }
        widgets['img'] = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
