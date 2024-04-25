from rest_framework.generics import ListAPIView

from core.filters import TransactionFilterSetClass, WalletFilterSetClass
from core.models import Transaction, Wallet
from core.serializers import TransactionListSerializer, WalletListSerializer

__all__ = [
    "TransactionListAPIView",
    "WallerListAPIView",
]


class TransactionListAPIView(ListAPIView):
    serializer_class = TransactionListSerializer
    filterset_class = TransactionFilterSetClass

    def get_queryset(self):
        return Transaction.objects.all()


class WallerListAPIView(ListAPIView):
    serializer_class = WalletListSerializer
    filterset_class = WalletFilterSetClass

    def get_queryset(self):
        return Wallet.objects.annotate_balance()
