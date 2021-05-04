from datetime import datetime, date, timedelta

from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist

from .models import Customer, Product, Sale, Location, SaleItem, CrmAdmin
from import_export import resources


@admin.register(CrmAdmin)
class CrmAdminAdmin(admin.ModelAdmin):
	pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	fieldsets = (
		('Meta Info', {
			'fields': ('created_by', 'date_created', 'date_to_be_contacted', 'location')
		}),
		('Contact Information', {
			'fields': ('first_name', 'last_name', 'mobile_number', 'email')
		}),
		('Preferred Method of Contact', {
			'fields': ('contact_call', 'contact_whatsapp', 'contact_email', 'do_not_contact')
		}),
		('PDPA (Personal Data Protection Act)', {
			'fields': ('pdpa_agreed',)
		}),
		('Customer Relations', {
			'fields': ('deal_stage', 'comments')
		}),
	)

	list_display = [
		'full_name',
		'mobile',
		'email',
		'stage',
		'created',
		'contact_date',
		'comments',
		'contact_via',
		'contact_on',
		'contact_status',
	]
	list_filter = [
		'created_by',
		'deal_stage',
		'date_created',
		'date_to_be_contacted',
	]
	search_fields = [
		'first_name',
		'last_name',
		'email',
		'comments'
	]

	def get_changeform_initial_data(self, request):
		from .models import CrmAdmin
		crm_settings = CrmAdmin.objects.all()[0]
		if not crm_settings:
			CrmAdmin.objects.create(
				default_add_date=date.today(),
				default_contact_date=date.today() + timedelta(days=7),
				use_defaults=True)
		if crm_settings.use_defaults:
			return {
				'created_by': request.user,
				'date_created': crm_settings.default_add_date,
				'date_to_be_contacted': crm_settings.default_contact_date,
			}
		else:
			return {
				'created_by': request.user,
			}

	def save_model(self, request, obj, form, change):
		"""
        Method to ensure saved customers will be automatically assigned to the creator.
        :param request: request object
        :param obj: instance of Customer
        :param form: N/A
        :param change: N/A
        :return: N/A
        """

		obj.created_by = request.user
		obj.save()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'price_sgd',
		'url',
		'is_free',
	]


class SaleItemInline(admin.TabularInline):
	model = SaleItem
	extra = 1


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
	list_display = [
		'date',
		'customer',
		'location',
		'invoice_total',
	]
	inlines = [
		SaleItemInline,
	]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	pass


class CustomerResource(resources.ModelResource):
	class Meta:
		model = Customer
		fields = ('email',)

