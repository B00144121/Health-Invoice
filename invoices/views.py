from django.shortcuts import render, redirect

from .models import Patient, Service, Invoice, InvoiceItem, Payment
from .forms import PatientForm, InvoiceForm, InvoiceItemForm, PaymentForm

def home(request):
    return render(request, 'home.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices.html', {'invoices': invoices})

def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            return redirect('add_invoice_items', invoice_id=invoice.id)
    else:
        form = InvoiceForm()
    return render(request, 'add_invoice.html', {'form': form})

def add_invoice_items(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    if request.method == 'POST':
        form = InvoiceItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.invoice = invoice
            item.save()
            return redirect('add_invoice_items', invoice_id=invoice.id)
    else:
        form = InvoiceItemForm()

    items = invoice.items.all()
    return render(request, 'add_invoice_items.html', {
        'invoice': invoice,
        'items': items,
        'form': form
    })

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = PaymentForm()
    return render(request, 'add_payment.html', {'form': form})

