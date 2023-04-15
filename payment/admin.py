from django.contrib import admin

# Register your models here.
from payment.models import Currency, Payment


admin.site.register(Currency)
admin.site.register(Payment)