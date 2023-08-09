from django import forms #added manually
from .models import *


class New_ad(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }