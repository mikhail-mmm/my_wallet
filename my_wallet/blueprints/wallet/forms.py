from wtforms_alchemy import ModelForm

from my_wallet.blueprints.wallet.models import Transaction


class TransactionAddForm(ModelForm):
    class Meta:
        model = Transaction
        only = ["timestamp", "amount", "currency", "description"]
