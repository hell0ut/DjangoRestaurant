from django import forms
from .models import *


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'