from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from payment import views

urlpatterns = [
    path('', views.PaymentList.as_view()),
    path('<str:reference_code>/', views.PaymentDetail.as_view()),
    path('currency/', views.CurrencyList.as_view()),
    path('pay/', views.ConfirmPayment.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)