from django import forms

from appmain.models import Reckoning


class AddPostForm(forms.Form):
    designer = forms.CharField(max_length=100)
    client_data = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=50)
    date = forms.DateField()

