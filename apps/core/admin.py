from django.contrib import admin

from core.models import Transaction, Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "label",
    ]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "txid",
        "wallet_id",
        "amount",
    ]
