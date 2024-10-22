from django.contrib import admin
from .models import Company, Shipping


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    fields = ['uuid', 'code', 'customer', 'company', 'product', 'weight', 'quantity', 'cost', 'source',
              'destination','is_paid', 'is_verified', 'is_active', 'is_received', 'describe', 'slug']
    readonly_fields = ['uuid', 'code']
    exclude = ['updated_at', 'created_at']
