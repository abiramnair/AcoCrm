from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver


class CrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm'
    verbose_name = 'CRM'
