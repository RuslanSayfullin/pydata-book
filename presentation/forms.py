from django import forms

from presentation.models import KitchenOfferpage


class AddKitchenOfferpageForm(forms.ModelForm):

    class Meta:
        model = KitchenOfferpage
        fields = ['upperfacades', 'lowerfacades', 'tabletop', 'other', 'accessories', 'sketch', 'costcalculation',
                  'total_price', 'total_discounted_price']





