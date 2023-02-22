from django import forms

from presentation.models import KitchenOfferpage


class AddKitchenOfferpageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    class Meta:
        model = KitchenOfferpage
        fields = [ 'upperfacades', 'lowerfacades', 'tabletop', 'other', 'accessories', 'sketch', 'costcalculation', 'total_price', 'total_discounted_price']
        widgets = {

            'upperfacades': forms.TextInput(attrs={'class': 'form-control'}),
            'lowerfacades': forms.TextInput(attrs={'class': 'form-control'}),
            'tabletop': forms.TextInput(attrs={'class': 'form-control'}),
            'other': forms.TextInput(attrs={'class': 'form-control'}),
            'accessories': forms.TextInput(attrs={'class': 'form-control'}),
            'total_price': forms.TextInput(attrs={'class': 'form-control'}),
            'total_discounted_price': forms.TextInput(attrs={'class': 'form-control'}),

        }





