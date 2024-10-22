from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from _resource.func import get_random_string


class Payment(models.Model):
    """Created for every payment in the website"""
    uuid = models.UUIDField(verbose_name=_('uuid'), default=uuid.uuid4, editable=False, blank=True)
    shipping = models.ForeignKey(verbose_name=_('shipping'),
                                 to='shipping.Shipping',
                                 related_name='payment_shipping',
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    code = models.CharField(verbose_name=_('code'), max_length=8, blank=True, editable=False)
    is_paid = models.BooleanField(verbose_name=_('is paid'), default=False)
    amount = models.DecimalField(verbose_name=_('amount'), max_digits=12, decimal_places=0)
    describe = models.TextField(verbose_name=_('describe'), blank=True)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)
    
    class Meta:
        ordering = ['-updated_at',]
        verbose_name = 'Payment'
        verbose_name_plural = 'Payment'
    
    def __str__(self):
        return f'payment_code:{self.code}'
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = get_random_string(8)
        return super().save(*args, **kwargs)
    
    @property
    def customer(self) -> object|None:
        """Get the customer the payment blongs to"""
        if self.shipping:
            return self.shipping.customer if self.shipping.customer else None
