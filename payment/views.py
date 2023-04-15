from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from payment.models import Currency, Payment
from payment.serializers import PaymentSerializer


class PaymentList(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        user = self.request.user
        return Payment.objects.filter(user=user)