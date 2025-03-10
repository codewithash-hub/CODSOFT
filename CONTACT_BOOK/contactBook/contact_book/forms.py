from django import forms
from .models import Contact_Information

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Information
        fields = ['name', 'phone', 'email', 'address']