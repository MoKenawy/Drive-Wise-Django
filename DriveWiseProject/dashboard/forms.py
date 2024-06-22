from django import forms
from django.forms import ImageField

class AddDriverForm(forms.Form):
    driver_id = forms.CharField(label='Driver ID', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    address = forms.CharField(label='Address', widget=forms.Textarea)
    birth_date = forms.DateField(label='Birth Date', widget=forms.SelectDateWidget(years=range(1900, 2025)))
    #photo = forms.ImageField(label='Photo', required=False)
    # photo = forms.FileField(label='Photo', required=False)


class RemoveDriverForm(forms.Form):
    driver_id = forms.CharField(label='Driver ID', max_length=100)

