# Generated by Django 3.2 on 2021-04-20 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_customer_time_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='time_created',
        ),
    ]
