from django import forms


class MyForm(forms.Form):
    # Define your form fields here
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    # Add more fields as needed


class CreateNewBillFile(forms.Form):
    billprice = forms.NumberInput()
    custbillfilenm = forms.CharField(label='Email')


class PaymentHistoryFilterForm(forms.Form):
    transaction_id = forms.CharField(required=False, label="Transaction ID")
    account_name = forms.CharField(required=False, label="Account Name")
    payment_mode = forms.CharField(required=False, label="Payment Mode")
    from_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    