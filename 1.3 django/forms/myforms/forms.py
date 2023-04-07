from django import forms
from django.core import validators
class FormName(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField( widget = forms.PasswordInput )
    botchecker = forms.CharField(required = False,
                                widget = forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])