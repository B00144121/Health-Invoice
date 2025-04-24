from django.test import TestCase
from .models import Patient, Service, Invoice

class PatientModelTest(TestCase):
    def test_create_patient(self):
        patient = Patient.objects.create(name="Fuad", email="fuad@test.com", phone="0871234567")
        self.assertEqual(patient.name, "Fuad")

class ServiceModelTest(TestCase):
    def test_service_price(self):
        service = Service.objects.create(name="Blood Test", price=25.50)
        self.assertEqual(service.price, 25.50)

class InvoiceModelTest(TestCase):
    def test_invoice_links_to_patient(self):
        patient = Patient.objects.create(name="Test Patient", email="test@example.com", phone="000000000")
        invoice = Invoice.objects.create(patient=patient)
        self.assertEqual(invoice.patient.name, "Test Patient")

