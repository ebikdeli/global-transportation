from django.test import TestCase
from shipping.models import Company, Shipping
from django.contrib.auth import get_user_model


class TestCompany(TestCase):
    """Test CRUD Company model"""
    def test_create_company(self):
        """Test if Company created successfully"""
        company_data = {'name': 'salaman', 'country': 'Iran'}
        company = Company.objects.create(**company_data)
        self.assertEqual(company.name, 'salaman')
    
    def test_delete_company(self):
        """Test if Company deleted successfully"""
        company_data = {'name': 'salaman', 'country': 'IR'}
        company, is_created = Company.objects.get_or_create(name='salaman', defaults=company_data)
        self.assertIn(company, Company.objects.all())
        Company.objects.filter(**company_data).delete()
        self.assertNotIn(company, Company.objects.all())
        
    def test_update_company(self):
        """Test if Company Updated successfully"""
        company_data = {'name': 'salaman', 'country': 'IR'}
        company, is_created = Company.objects.get_or_create(name='salaman', defaults=company_data)
        # print(company.country.name)
        self.assertEqual([company.name, company.country.name], ['salaman', 'Iran'])
        Company.objects.filter(**company_data).update(name='jake', country='AE')
        company.refresh_from_db()
        self.assertEqual([company.name, company.country.name], ['jake', 'United Arab Emirates'])


class TestShipping(TestCase):
    """Test CRUD of Shipping model"""
    def setUp(self):
        customer_data = {'username': 'ehsan', 'password': '123', 'email': 'ebikdeli@gmail.com'}
        self.customer = get_user_model().objects.create_user(**customer_data)
        company_data = {'name': 'salaman company', 'country': 'US', 'establish': '2012'}
        self.company = Company.objects.create(**company_data)
    
    def test_create_shipping(self):
        """Test if Shipping created successfully"""
        shipping_data = {'customer': self.customer, 'company': self.company, 'product': 'Video gaming consoles',
                         'quantity': 15, 'cost': 15000000 , 'source': 'Ahwaz', 'destination': 'Dubai'}
        shipping = Shipping.objects.create(**shipping_data)
        self.assertIsNotNone(shipping)
        
    def test_delete_shipping(self):
        """Test if Shipping deleted successfully"""
        shipping_data = {'customer': self.customer, 'company': self.company, 'product': 'Video gaming consoles',
                         'quantity': 15, 'cost': 15000000 , 'source': 'Ahwaz', 'destination': 'Dubai'}
        shipping = Shipping.objects.create(**shipping_data)
        self.assertIn(shipping, Shipping.objects.all())
        Shipping.objects.filter(customer=self.customer).delete()
        self.assertNotIn(shipping, Shipping.objects.all())
    
    def test_update_shipping(self):
        """Test if shipping updated successfully"""
        shipping_data = {'customer': self.customer, 'company': self.company, 'product': 'Video gaming consoles',
                         'quantity': 15, 'cost': 15000000 , 'source': 'Ahwaz', 'destination': 'Dubai'}
        shipping = Shipping.objects.create(**shipping_data)
        self.assertEqual(shipping.product, 'Video gaming consoles')
        Shipping.objects.filter(customer=self.customer).update(**{'product': 'Digital Scanner'})
        shipping.refresh_from_db()
        self.assertEqual(shipping.product, 'Digital Scanner')
