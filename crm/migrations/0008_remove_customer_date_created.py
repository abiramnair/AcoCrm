# Generated by Django 3.2 on 2021-04-20 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_alter_customer_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date_created',
        ),
    ]
