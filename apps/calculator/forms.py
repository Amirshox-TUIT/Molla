from django import forms
from apps.calculator.models import CalculatorModel


class CalculatorForm(forms.ModelForm):
    class Meta:
        model = CalculatorModel
        exclude = ['result']
