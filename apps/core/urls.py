from django.urls import path

from core.views import TransactionListAPIView, WallerListAPIView

app_name = "core"

urlpatterns = [
    path(
        route="wallet/",
        view=WallerListAPIView.as_view(),
        name="wallets"
    ),
    path(
        route="transactions/",
        view=TransactionListAPIView.as_view(),
        name="transactions",
    ),
]
