from rest_framework import serializers

from core.models import Transaction, Wallet


class TransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields: list[str] = [
            "id",
            "wallet_id",
            "txid",
            "amount",
        ]


class WalletListSerializer(serializers.ModelSerializer):
    balance = serializers.ReadOnlyField(source="_balance")

    class Meta:
        model = Wallet
        fields: list[str] = [
            "id",
            "label",
            "balance",
        ]
