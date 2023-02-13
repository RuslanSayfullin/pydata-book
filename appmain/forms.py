from django import forms
from django.contrib.auth.models import User


class PrettyModelChoiceField(forms.ModelChoiceField):
    # Show pretty user name
    def label_from_instance(self, user):
        user = user.get_full_name()
        return super(PrettyModelChoiceField, self).label_from_instance(user)


class NewReckoningForm(forms.Form):
    designer = PrettyModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'selectpicker show-tick'}))
    client_data = forms.CharField(initial="")
    phone = forms.CharField(initial="")
    date = forms.DateTimeField(input_formats=['%d.%m.%Y'], initial="")

    def clean_designer(self):
        designer = self.cleaned_data['designer']
        if not designer in User.objects.all():
            raise forms.ValidationError(u'Такого дизайнера не существует')
        return self.cleaned_data['designer']




