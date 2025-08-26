from django import forms
from apps.pages.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude= ['created', 'is_read']