from django import forms
from .models import product,Reviews
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'Enter your first name','required': "required",
                                                       "data-validation-required-message": "Please enter a first name"})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Enter your last name','required': "required",
                                                       "data-validation-required-message": "Please enter a Last name"})
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter your username','required': "required",
                                                       "data-validation-required-message": "Please enter a username"})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Enter your email','required': "required",
                                                       "data-validation-required-message": "Please enter a Email"})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Enter your password','required': "required",
                                                       "data-validation-required-message": "Please enter a password"})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Enter your confirm password','required': "required",
                                                       "data-validation-required-message": "Please enter a password"})


class UserProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'Enter your first name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Enter your last name'})
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter your username'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Enter your email'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'Enter your Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'Enter your Again Password'})

class ProductsForm(forms.ModelForm):
    class Meta:
        model = product
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['product_review'].widget.attrs.update({'class':'form-control'})   
        self.fields['reviews'].widget.attrs.update({'class':'form-control','placeholder':"Enter your review"})
        self.fields['name'].widget.attrs.update({'class':'form-control','placeholder':"Enter your name"})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':"Enter your email"})   

