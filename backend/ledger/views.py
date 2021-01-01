from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer, UserSerializer
from .permissions import IsSuperUserOrReadOnly

# Create your views here.
class AccountAPIViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TransactionAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsSuperUserOrReadOnly,) # new
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class UserAPIViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

