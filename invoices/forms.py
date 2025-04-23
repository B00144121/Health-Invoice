from django import forms
from .models import Patient, Invoice, InvoiceItem, Payment

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'phone']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['patient']

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['service', 'quantity']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['invoice', 'amount_paid', 'method']
