from django.http import Http404, QueryDict
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.exceptions import ParseError, PermissionDenied
from rest_framework.response import Response
from rest_framework import generics, status

from payment.models import Currency, Payment
from payment.serializers import CurrencySerializer, PaymentSerializer, CreatePaymentSerializer
from user.serializers import PaymentUserSerializer


class PaymentList(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        user = self.request.user
        reference = self.request.query_params.get('reference')
        currency = self.request.query_params.get('currency')

        queryset = Payment.objects.prefetch_related('currency').filter(user=user)
        if reference is not None:
            queryset = queryset.filter(reference_code=reference)
        if currency is not None:
            queryset = queryset.filter(currency__code=currency)
        return queryset

    def create(self, request, *args, **kwargs):

        try:
            data = QueryDict('', mutable=True)
            data.update(request.data)
            data.update(user=request.user.id, currency=Currency.objects.get(code=data.get("currency")).id)

            serializer = CreatePaymentSerializer(data=data)
        except Exception as e:
            raise ParseError("Invalid Currency code")

        serializer.is_valid(raise_exception=True)

        # FUNCTION TO CHECK FOR OVERDRAFT
        is_payment_beyond_limit = serializer.is_payment_beyond_limit(self.request)
        if is_payment_beyond_limit is not None:
            raise PermissionDenied(detail=is_payment_beyond_limit.get('detail'))

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PaymentDetail(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    lookup_field = 'reference_code'

    def get_object(self):
        queryset = self.get_queryset()
        filter = {
            self.lookup_field: self.kwargs[self.lookup_field],
            'user': self.request.user.id
        }

        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj


class CurrencyList(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ConfirmPayment(APIView):
    """
    """

    def post(self, request, format=None):
        try:
            reference_code = request.data.get('reference_code')
            payment = Payment.objects.get(reference_code=reference_code)
        except Exception as e:
            raise ParseError("Invalid reference code")

        if payment.is_paid:
            raise PermissionDenied(detail="Transaction has already been paid")
        else:
            payment.is_paid = True
            payment.save()

            serializer = PaymentSerializer(payment)
            return Response(serializer.data)