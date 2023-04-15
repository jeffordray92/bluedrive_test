import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

optional = {
    'blank': True,
    'null': True
}

def generate_ref_code(digits):
    code = str(uuid.uuid4()).replace("-","")[:digits]
    return code

class Currency(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=3, unique=True, **optional) # TODO: ADD UNIQUE
    created_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now().date())

    def save(self, *args, **kwargs):
        code = generate_ref_code(3)
        self.reference_code = code
        super(Currency, self).save(*args, **kwargs)

    def __str__(self):
        return "{} ({})".format(self.name, self.code)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reference_code = models.CharField(max_length=10, unique=True, **optional)
    amount = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(**optional)
    created_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now().date())

    def save(self, *args, **kwargs):
        code = generate_ref_code(10)
        self.reference_code = code
        super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {} by {} ({})".format(
            self.amount,
            self.currency.code,
            self.user.username,
            self.created_date
        )

