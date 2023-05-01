from django import forms
from django.forms import fields
from .models import Contact_Info

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Info
        fields = '__all__'