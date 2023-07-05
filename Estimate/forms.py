from django import forms
from .models import Estimate

class EstimateForm(forms.ModelForm):
    class Meta:
        model = Estimate
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['apartment_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['bedroomes_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['modular_kitchen'].widget.attrs.update({'class': 'form-control'})
        self.fields['Carpet_area_in_sqft'].widget.attrs.update({'class': 'form-control'})

        