from django.shortcuts import render
from rest_framework import generics

from ledger.models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer

# Create your views here.
class AccountAPIListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountAPIDetailView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransactionAPIListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionAPIDetailView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

