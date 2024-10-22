from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.conf import settings
from django_countries.fields import CountryField
import uuid
from _resource.func import get_random_string


class Company(models.Model):
    """Model that represents a shipping company"""
    name = models.CharField(verbose_name=_('name'), max_length=50)
    country = CountryField(verbose_name=_('country'), blank=True)
    descibe = models.TextField(verbose_name=_('describe'), blank=True)
    establish = models.CharField(verbose_name=_('establish'), max_length=4, blank=True)
    slug = models.SlugField(blank=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Company'
        verbose_name_plural = 'Company'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Shipping(models.Model):
    """Model to represend the shipping process"""
    uuid = models.UUIDField(verbose_name=_('uuid'), default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(verbose_name=_('customer'),
                                 to=settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_NULL,
                                 related_name='shipping_customer',
                                 blank=True,
                                 null=True)
    company = models.ForeignKey(verbose_name=_('company'),
                                to='shipping.Company',
                                on_delete=models.SET_NULL,
                                related_name='shipping_company',
                                blank=True,
                                null=True)
    code = models.CharField(verbose_name=_('code'), max_length=8, blank=True, editable=False)
    product = models.CharField(verbose_name=_('product'), max_length=100)
    weight = models.FloatField(verbose_name=_('weight'), default=0)
    quantity = models.IntegerField(verbose_name=_('quantity'), default=0)
    cost = models.DecimalField(verbose_name=_('cost'), max_digits=12, decimal_places=0, default=0)
    source = models.CharField(verbose_name=_('source'), max_length=50)
    destination = models.CharField(verbose_name=_('destination'), max_length=50)
    is_paid = models.BooleanField(verbose_name=_('is paid'), default=False)
    is_active = models.BooleanField(verbose_name=_('is active'), default=False)
    is_verified = models.BooleanField(verbose_name=_('is verified'), default=False)
    is_received = models.BooleanField(verbose_name=_('is received'), default=False)
    describe = models.TextField(verbose_name=_('describe'), blank=True)
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Shipping'
        verbose_name_plural = 'Shipping'
    
    def __str__(self):
        return f'shipping code: {self.code}'
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(8)
        if not self.slug:
            self.slug = slugify(f'shipping code {self.code}')
        return super().save(*args, **kwargs)
