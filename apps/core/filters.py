import django_filters as filters

from core.models import Transaction, Wallet


class TransactionFilterSetClass(filters.FilterSet):
    order_by = filters.OrderingFilter(
        fields=(("amount", "amount"),), field_labels={"amount": "Amount"}
    )

    class Meta:
        model = Transaction
        fields: list[str] = [
            "wallet_id",
            "txid",
        ]


class WalletFilterSetClass(filters.FilterSet):
    order_by = filters.OrderingFilter(
        fields=(("_balance", "_balance"),), field_labels={"_balance": "Balance"}
    )

    class Meta:
        model = Wallet
        fields: list[str] = [
            "label",
        ]
