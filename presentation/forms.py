from django import forms

from presentation.models import KitchenOfferpage


class AddKitchenOfferpagePostForm(forms.ModelForm):

    class Meta:
        model = KitchenOfferpage
        fields = '__all__'

