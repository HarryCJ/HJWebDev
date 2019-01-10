from django import forms

class ContactForm(forms.Form):
        
    name = forms.CharField(label='Your name:', max_length=100)
    email = forms.CharField(label='Your email:', max_length=100)
    message = forms.CharField(label='Your message:', max_length=500, widget=forms.Textarea)