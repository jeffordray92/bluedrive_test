from django.contrib.auth.models import User
from django.db import models

optional = {
    'blank': True,
    'null': True
}

class Currency(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=3) # TODO: ADD UNIQUE
    created_date = models.DateField(auto_now=False, auto_now_add=False)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reference_code = models.CharField(max_length=10) # TODO: ADD UNIQUE
    amount = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(**optional)
    created_date = models.DateField(auto_now=False, auto_now_add=False)