from typing import Self

from django.db import models
from django.db.models.constraints import UniqueConstraint


class Transaction(models.Model):
    wallet = models.ForeignKey(
        "Wallet",
        related_name="transactions",
        on_delete=models.SET_NULL,
        null=True,
    )
    txid = models.CharField(
        max_length=128
    )
    amount = models.DecimalField(
        max_digits=18, decimal_places=2
    )

    class Meta:
        constraints = [
            UniqueConstraint(fields=["txid"], name="unique_txid"),
        ]

    def __str__(self) -> str:
        return f"{self.id}: {self.txid}"


class WalletQuerySet(models.QuerySet):
    def annotate_balance(self) -> Self:
        return self.annotate(_balance=models.Sum("transactions__amount"))


class Wallet(models.Model):
    label = models.CharField(
        max_length=128
    )

    objects = WalletQuerySet.as_manager()

    def __str__(self) -> str:
        return self.label
