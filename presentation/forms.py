from django import forms

from presentation.models import KitchenOfferpage


class AddKitchenOfferpagePostForm(forms.Form):
    upperfacades = forms.CharField(
        required=False, max_length=200, label='Фасады (верх)',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фасады (верх)'}))
    lowerfacades = forms.CharField(
        required=False, max_length=200, label='Фасады (низ)',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фасады (низ)'}))
    tabletop = forms.CharField(
        required=False, max_length=200, label='Столешница',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Столешница'}))
    other = forms.CharField(
        required=False, max_length=200, label='Прочее',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Прочее'}))
    accessories = forms.CharField(
        required=False, max_length=200, label='Фурнитура',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фурнитура'}))
    sketch = forms.ImageField(
        required=False, label='Эскиз',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Эскиз'}))
    costcalculation = forms.FileField(required=False, label='Расчёт себестоимости',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Расчёт себестоимости'}))
    total_price = forms.IntegerField(
        required=False, max_value=2147483647, min_value=0, label='Всего к оплате в рублях',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '100000',
                                      'title': 'Итоговая сумма договора по товарному чеку, цифрами',
                                      'onkeyup': 'oplata_predoplata_and_ostatok();'}))
    total_discounted_price = forms.IntegerField(
        required=False, max_value=2147483647, min_value=0, label='Стоимость со скидкой',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '100000',
                                      'title': 'Стоимость со скидкой',
                                      'onkeyup': 'oplata_predoplata_and_ostatok();'}))


class AddKitchenOfferpageForm(forms.ModelForm):
    class Meta:
        model = KitchenOfferpage
        fields = ['reckoning', 'upperfacades', 'lowerfacades', 'tabletop', 'other', 'accessories', 'sketch', 'costcalculation', 'total_price', 'total_discounted_price']




