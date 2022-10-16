from django import forms
from .models import Item

# Create the form class.


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
        # '__all__' for all of them
