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