from flask import current_app

from my_wallet.blueprints.wallet.models import Wallet


def create_wallet(wallet: Wallet):
    current_app.session.add(wallet)
    current_app.session.commit()
