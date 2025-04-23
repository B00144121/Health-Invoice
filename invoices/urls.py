from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/add/', views.add_invoice, name='add_invoice'),
    path('invoices/<int:invoice_id>/items/', views.add_invoice_items, name='add_invoice_items'),
    path('payments/add/', views.add_payment, name='add_payment'),
]