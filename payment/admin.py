from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fields = ['uuid', 'code', 'shipping', 'is_paid', 'amount', 'describe']
    readonly_fields = ['uuid', 'code']
    exclude = ['created_at', 'updated_at']
