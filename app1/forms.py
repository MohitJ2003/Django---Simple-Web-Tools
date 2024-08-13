from django import forms


class MyForm(forms.Form):
    # Define your form fields here
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    # Add more fields as needed


class CreateNewBillFile(forms.Form):
    billprice = forms.NumberInput()
    custbillfilenm = forms.CharField(label='Email')
