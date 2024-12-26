from django.test import TestCase
from django.core.exceptions import ValidationError
from account.models import Address
from dodobed_warehouse_systems.planner.models import Customer

class CustomerModelTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            street="123 Main St",
            city="Anytown",
            state="Anystate",
            postal_code="12345",
            country="Country"
        )

    def test_create_customer(self):
        customer = Customer.objects.create(
            customer_name="John Doe",
            contact=self.address,
            priority_level="High"
        )
        self.assertEqual(customer.customer_name, "John Doe")
        self.assertEqual(customer.contact, self.address)
        self.assertEqual(customer.priority_level, "High")

    def test_customer_priority_choices(self):
        customer = Customer.objects.create(
            customer_name="Jane Doe",
            contact=self.address,
            priority_level="Medium"
        )
        self.assertIn(customer.priority_level, dict(Customer.PRIORITY_CHOICES))

    def test_customer_str_method(self):
        customer = Customer.objects.create(
            customer_name="John Smith",
            contact=self.address,
            priority_level="Low"
        )
        self.assertEqual(str(customer), "John Smith")

    def test_invalid_priority_level(self):
        with self.assertRaises(ValidationError):
            customer = Customer(
                customer_name="Invalid Priority",
                contact=self.address,
                priority_level="Invalid"
            )
            customer.full_clean()  # This will trigger the validation