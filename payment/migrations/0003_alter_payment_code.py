# Generated by Django 5.1.1 on 2024-10-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_payment_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='code',
            field=models.CharField(blank=True, editable=False, max_length=8, verbose_name='code'),
        ),
    ]
