# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class KeyForm(forms.Form):
    key = forms.CharField(max_length=100)

class CipherForm(forms.Form):
    cipher = forms.CharField(max_length=100)
