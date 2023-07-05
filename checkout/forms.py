from django import forms
from .models import CheckOut

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = CheckOut
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':"Enter your first name"})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':"Enter your Last name"})
        # self.fields['middle_name'].widget.attrs.update({'class':'form-control','placeholder':"Enter your Middle name"})
        self.fields['address'].widget.attrs.update({'class':'form-control','placeholder':"Enter your Address"})
        # self.fields['checkout_email'].widget.attrs.update({'class':'form-control','placeholder':"Enter your Email"})
        # self.fields['product_qty'].widget.attrs.update({'class':'form-control','placeholder':"Enter your Product_qty"})
        # self.fields['products_id'].widget.attrs.update({'class':'form-control','placeholder':"Enter your Product_ID"})
        # self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':"Enter your Username"})
        # self.fields['status'].widget.attrs.update({'class':'form-control','placeholder':"Enter your status"})