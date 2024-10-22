from django.test import TestCase
from django.contrib.auth import get_user_model
from shipping.models import Company, Shipping
from .models import Payment


class PaymentTest(TestCase):
    """Test Payment model"""
    def setUp(self):
        _customer_data = {'username': 'ehsan', 'password': '123', 'email': 'ebikdeli@gmail.com'}
        self.customer = get_user_model().objects.create_user(**_customer_data)
        _company_data = {'name': 'salaman company', 'country': 'US', 'establish': '2012'}
        self.company = Company.objects.create(**_company_data)
        _shipping_data = {'customer': self.customer, 'company': self.company, 'product': 'Video gaming consoles',
                         'quantity': 15, 'cost': 15000000 , 'source': 'Ahwaz', 'destination': 'Dubai'}
        self.shipping = Shipping.objects.create(**_shipping_data)
    
    def test_create_payment(self):
        """Test Payment creation"""
        payment = Payment.objects.create(shipping=self.shipping, amount=1400000)
        self.assertIn(payment, Payment.objects.all())
    
    def test_delete_payment(self):
        """Test Payment delete"""
        payment = Payment.objects.create(shipping=self.shipping, amount=1400000)
        self.assertIn(payment, Payment.objects.all())
        payment.delete()
        self.assertNotIn(payment, Payment.objects.all())
    
    def test_update_payment(self):
        """Test payment update"""
        payment = Payment.objects.create(shipping=self.shipping, amount=1400000)
        self.assertEqual(payment.amount, 1400000)
        Payment.objects.update_or_create(id=payment.id, defaults={'amount': 1600000})
        payment.refresh_from_db()
        self.assertEqual(payment.amount, 1600000)
    
    def test_payment_without_shipping(self):
        """Test if Payment works without shipping"""
        payment = Payment.objects.create(shipping=self.shipping, amount=1400000)
        self.assertEqual(payment.shipping, self.shipping)
        self.shipping.delete()
        payment.refresh_from_db()
        self.assertEqual(payment.shipping, None)
