# Generated by Django 5.1.1 on 2024-10-22 16:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0003_alter_shipping_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='is verified'),
        ),
        migrations.AddField(
            model_name='shipping',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, verbose_name='uuid'),
        ),
    ]
