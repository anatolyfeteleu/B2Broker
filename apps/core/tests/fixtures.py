import pytest

from core.models import Transaction, Wallet
from core.tests.factories import (
    WalletFactory,
    TransactionFactory,
    WalletWithTransactionsFactory,
)


@pytest.fixture()
def wallets_with_transactions(request) -> list[Wallet]:
    count: int = request.param if hasattr(request, "param") else 1
    return [WalletWithTransactionsFactory() for _ in range(count)]


@pytest.fixture()
def wallets(request) -> list[Wallet]:
    count: int = request.param if hasattr(request, "param") else 1
    return [WalletFactory() for _ in range(count)]


@pytest.fixture()
def transactions(request) -> list[Transaction]:
    count: int = request.param if hasattr(request, "param") else 1
    return [TransactionFactory() for _ in range(count)]
