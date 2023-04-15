# Generated by Django 4.2 on 2023-04-15 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_payment_paid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(blank=True, max_length=3, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='created_date',
            field=models.DateField(default=datetime.date(2023, 4, 15)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_date',
            field=models.DateField(default=datetime.date(2023, 4, 15)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='reference_code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]