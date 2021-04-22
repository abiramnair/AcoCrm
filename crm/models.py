from datetime import timedelta, date

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.datetime_safe import strftime, datetime

from .constants import DEAL_STAGES, PREFERRED_METHOD_OF_CONTACT
from .validators import mobile_number_validator, discount_validator
from django.utils.html import mark_safe

User = get_user_model()


class Customer(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Alexandr&Co. Staff Member who served this customer."
    )
    date_created = models.DateField(default=date.today, null=True, blank=True)
    time_created = models.TimeField(auto_now_add=True, null=True, blank=True)
    date_to_be_contacted = models.DateField(
        null=True,
        blank=True,
        default=date.today() + timedelta(days=7),
        help_text='DO NOT EDIT. Only change if the customer request to be contacted on a different day. Default is 7 '
                  'days. '
    )
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    mobile_number = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        validators=[mobile_number_validator, ]
    )
    email = models.EmailField(null=True, blank=True)
    contact_call = models.BooleanField(default=False)
    contact_whatsapp = models.BooleanField(default=False)
    contact_email = models.BooleanField(default=False)
    do_not_contact = models.BooleanField(default=False, verbose_name='DO NOT CONTACT')
    pdpa_agreed = models.BooleanField(
        help_text='Customer has agreed to PDPA rules.',
        verbose_name='PDPA Acknowledged'
    )
    deal_stage = models.CharField(
        max_length=50,
        choices=DEAL_STAGES,
        null=True,
        blank=True,
        default='interested',
    )
    comments = models.TextField(null=True, blank=True)

    @property
    def mobile(self):
        return self.mobile_number

    @property
    def created(self):
        return self.date_created

    @property
    def contact_date(self):
        return self.date_to_be_contacted

    @property
    def stage(self):
        return mark_safe('<strong style="color:#5a8dee;">%s</strong>' % self.deal_stage.title())

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def contact_on(self):
        return self.date_created + timedelta(days=7)

    @property
    def contact_via(self):
        methods = (
            ('Email', self.contact_email),
            ('Whatsapp', self.contact_whatsapp),
            ('Call', self.contact_call),
            ('Do Not Contact', self.do_not_contact),
        )
        return [m[0] for m in methods if m[1]]

    @property
    def contact_status(self):
        if not self.deal_stage == 'closed lost':
            if self.date_to_be_contacted < date.today():
                return mark_safe('<strong style="color:red;">OVERDUE</strong>')
            elif self.date_to_be_contacted == date.today():
                return mark_safe('<strong>TODAY</strong>')
            else:
                return f"Due in {(self.date_to_be_contacted - date.today()).days} days."
        else:
            return mark_safe('<strong style="color:red;">DO NOT CONTACT</strong>')

    def __str__(self):
        return self.full_name


class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Sale(models.Model):
    staff = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    date = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    invoice_total = models.DecimalField(default=0,
                                        decimal_places=2,
                                        max_digits=10,
                                        null=True,
                                        blank=True,
                                        editable=False
                                        )

    def __str__(self):
        return f"{self.date.strftime('%d %b %y')}"


class Product(models.Model):
    name = models.CharField(max_length=55)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    url = models.URLField(null=True, blank=True)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def price_sgd(self):
        return f"${self.price}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_free:
            self.price = 0.00
        super().save(*args, **kwargs)


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    selling_price = models.DecimalField(decimal_places=2, max_digits=10)
