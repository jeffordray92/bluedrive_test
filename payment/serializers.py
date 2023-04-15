from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import serializers, permissions

from payment.models import Currency, Payment


# class CurrencySerializer(serializers.Serializer):
#     class Meta:
#         model = Currency
#         fields = [
#             'name',
#             'code'
#         ]


class PaymentSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username')
    currency_code = serializers.CharField(source='currency.code')

    class Meta:
        model = Payment
        fields = [
            'user',
            'username',
            'reference_code',
            'amount',
            'currency_code',
            'is_paid',
            'paid_date',
            'created_date'
        ]