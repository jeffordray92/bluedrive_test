from django.db.models import Sum
from django.utils import timezone

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import serializers, permissions

from payment.models import Currency, Payment
from user.serializers import PaymentUserSerializer

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            'name',
            'code'
        ]


class PaymentSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    user = PaymentUserSerializer()

    class Meta:
        model = Payment
        fields = [
            'user',
            'reference_code',
            'amount',
            'currency',
            'is_paid',
            'paid_date',
            'created_date'
        ]


class CreatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def is_payment_beyond_limit(self, request, **kwargs):
        total_daily_transaction = Payment.objects.filter(
            user=request.user,
            created_date=timezone.now().date(),
            currency=self.validated_data.get('currency')
        ).aggregate(Sum('amount', default=0)).get('amount__sum')
        if self.validated_data.get('amount') + total_daily_transaction > 5000:
            return {
                "error": True,
                "detail": "Transaction goes beyond daily amount limit for this currency. Total daily transactions = {} {}".format(
                    total_daily_transaction,
                    self.validated_data.get('currency').code
                )
            }
        else: return None