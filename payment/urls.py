from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from payment import views

urlpatterns = [
    path('', views.PaymentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)