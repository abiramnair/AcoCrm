# Generated by Django 3.2 on 2021-04-21 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20210421_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='location',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='saleitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='saleitem',
            name='sale',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.DeleteModel(
            name='SaleItem',
        ),
    ]
