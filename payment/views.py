from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from payment.models import Currency, Payment
from payment.serializers import CurrencySerializer, PaymentSerializer


class PaymentList(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        user = self.request.user
        reference = self.request.query_params.get('reference')
        currency = self.request.query_params.get('currency')
        queryset = Payment.objects.filter(user=user)
        if reference is not None:
            queryset = queryset.filter(reference_code=reference)
        if currency is not None:
            queryset = queryset.filter(currency__code=currency)
        return queryset

class CurrencyList(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer