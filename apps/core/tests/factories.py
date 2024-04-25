import uuid
from decimal import Decimal
from random import randint

import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from core.models import Transaction, Wallet


class WalletFactory(DjangoModelFactory):
    label = fuzzy.FuzzyText(length=128)

    class Meta:
        model = Wallet


class WalletWithTransactionsFactory(WalletFactory):

    @factory.post_generation
    def transactions(self, create, extracted, **kwargs):
        if not create:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        for _ in range(10):
            TransactionFactory(wallet=self)


class TransactionFactory(DjangoModelFactory):
    wallet = factory.SubFactory("apps.core.tests.factories.WalletFactory")
    txid = factory.LazyFunction(lambda: uuid.uuid4().hex)
    amount = factory.LazyFunction(lambda: Decimal(randint(0, 100_000)))

    class Meta:
        model = Transaction
