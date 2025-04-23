from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Patient, Service, Invoice, InvoiceItem, Payment

admin.site.register(Patient)
admin.site.register(Service)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Payment)
