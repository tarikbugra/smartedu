from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    fname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'First Name'
        }))
    lname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Last Name'
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
         'placeholder': 'Email'
        }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Phone'
        }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 
        'placeholder': 'Message'
        }))

    class Meta:
        model = Contact
        fields = ['fname', 'lname', 'email', 'phone', 'message']
