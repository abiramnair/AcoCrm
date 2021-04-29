# Generated by Django 3.2 on 2021-04-26 00:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0020_auto_20210425_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gid',
            field=models.CharField(default='', editable=False, max_length=55),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_to_be_contacted',
            field=models.DateField(blank=True, default=datetime.date(2021, 5, 3), help_text='DO NOT EDIT. Only change if the customer request to be contacted on a different day. Default is 7 days. ', null=True),
        ),
    ]