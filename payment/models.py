from django.contrib.auth.models import User
from django.db import models

is_required = {
    'blank': False,
    'null': False
}

class Currency(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=3) # TODO: ADD UNIQUE
    created_date = models.DateField(auto_now=False, auto_now_add=False)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reference_code = models.CharField(max_length=10) # TODO: ADD UNIQUE
    amount = models.FloatField(**is_required)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField()
    created_date = models.DateField(auto_now=False, auto_now_add=False)