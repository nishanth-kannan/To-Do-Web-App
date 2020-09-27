from django import forms
from .models import List

#the form which is based off the model List
class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed']
