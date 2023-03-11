from django.shortcuts import render
from rest_framework import viewsets
from api.models import AllCustomers , TransactionHistory
from api.serializers import CustomerSerializers , TransactionSerializers

# Create your views here.


class CustomerViewset(viewsets.ModelViewSet):
    queryset= AllCustomers.objects.all()
    serializer_class=CustomerSerializers

class TransactionViewset(viewsets.ModelViewSet):
    queryset= TransactionHistory.objects.all()
    serializer_class=TransactionSerializers