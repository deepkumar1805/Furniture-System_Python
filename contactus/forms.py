from django import forms
from .models import Contactus

class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control','placeholder':"Enter your name"})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':"Enter your email"})
        self.fields['subject'].widget.attrs.update({'class':'form-control','placeholder':"Enter your subject"})
        self.fields['msg'].widget.attrs.update({'class':'form-control','placeholder':"Enter your msg"})