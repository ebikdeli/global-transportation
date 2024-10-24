from django import forms
from .models import Shipping


class ShippingModelForm(forms.ModelForm):
    """ModelForm for Shipping"""
    
    class Meta:
        model = Shipping
        exclude = ['customer', 'cost', 'is_active',
                   'is_verified', 'is_paid', 'is_received',
                   'slug',]
