from typing import Optional

import pytest
from django.db import models
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class TestGetWalletListView:
    PATH = "api:core:wallets"

    @staticmethod
    def _get_api_client() -> APIClient:
        credentials = {"HTTP_ACCEPT": "application/json;"}
        api_client = APIClient()
        api_client.credentials(**credentials)
        return api_client

    def _do_request(self, data: Optional[dict] = None):
        api_client = self._get_api_client()
        return api_client.get(path=reverse(self.PATH), data=data)

    @pytest.mark.parametrize(
        "wallets_with_transactions",
        [2],
        indirect=["wallets_with_transactions"],
    )
    def test_successful_request(self, wallets_with_transactions):
        response = self._do_request()

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    @pytest.mark.parametrize(
        "wallets_with_transactions",
        [5],
        indirect=["wallets_with_transactions"],
    )
    def test_balance(self, wallets_with_transactions):
        response = self._do_request()

        wallet = wallets_with_transactions[0]
        transactions = wallet.transactions
        total_amount = transactions.aggregate(
            total_amount=models.Sum("amount")
        )["total_amount"]

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 5

        wallet_from_response = next(
            filter(lambda x: x["id"] == wallet.id, response.data)
        )

        assert wallet_from_response["balance"] == total_amount

    @pytest.mark.parametrize(
        "wallets_with_transactions",
        [2],
        indirect=["wallets_with_transactions"],
    )
    def test_desc_ordering(self, wallets_with_transactions):
        response = self._do_request(data={"order_by": "-_balance"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]["balance"] > response.data[1]["balance"]

    @pytest.mark.parametrize(
        "wallets_with_transactions",
        [2],
        indirect=["wallets_with_transactions"],
    )
    def test_asc_ordering(self, wallets_with_transactions):
        response = self._do_request(data={"order_by": "_balance"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data[0]["balance"] < response.data[1]["balance"]

    @pytest.mark.parametrize(
        "wallets_with_transactions",
        [2],
        indirect=["wallets_with_transactions"],
    )
    def test_searching_by_label(self, wallets_with_transactions):
        wallet = wallets_with_transactions[0]
        response = self._do_request(data={"label": wallet.label})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["label"] == wallet.label


class TestGetTransactionListView:
    PATH = "api:core:transactions"

    @staticmethod
    def _get_api_client() -> APIClient:
        credentials = {"HTTP_ACCEPT": "application/json;"}
        api_client = APIClient()
        api_client.credentials(**credentials)
        return api_client

    def _do_request(self, data: Optional[dict] = None):
        api_client = self._get_api_client()
        return api_client.get(path=reverse(self.PATH), data=data)

    @pytest.mark.parametrize("transactions", [10], indirect=["transactions"])
    def test_successful_request(self, transactions):
        response = self._do_request()

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10

    @pytest.mark.parametrize("transactions", [10], indirect=["transactions"])
    def test_desc_ordering_by_amount(self, transactions):
        response = self._do_request(data={"order_by": "-amount"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10
        assert response.data[0]["amount"] > response.data[1]["amount"]

    @pytest.mark.parametrize("transactions", [10], indirect=["transactions"])
    def test_asc_ordering_by_amount(self, transactions):
        response = self._do_request(data={"order_by": "amount"})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10
        assert response.data[0]["amount"] < response.data[1]["amount"]

    @pytest.mark.parametrize("transactions", [10], indirect=["transactions"])
    def test_searching_by_wallet_id(self, transactions):
        transaction = transactions[0]
        response = self._do_request(data={"wallet_id": transaction.wallet_id})

        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]["wallet_id"] == transaction.wallet_id

    @pytest.mark.parametrize("transactions", [10], indirect=["transactions"])
    def test_searching_by_txid(self, transactions):
        transaction = transactions[0]
        response = self._do_request(data={"txid": transaction.txid})

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["txid"] == transaction.txid
