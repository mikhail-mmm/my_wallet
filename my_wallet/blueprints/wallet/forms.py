from wtforms_alchemy import ModelForm

from my_wallet.blueprints.wallet.models import Transaction, Wallet


class TransactionAddForm(ModelForm):
    class Meta:
        model = Transaction
        only = ["timestamp", "amount", "currency", "description"]


class WalletAddForm(ModelForm):
    class Meta:
        model = Wallet
        only = ["title"]
