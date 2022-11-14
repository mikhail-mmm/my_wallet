from flask import current_app

from my_wallet.blueprints.wallet.models import Wallet


def create_wallet(wallet: Wallet):
    return create(wallet)


def create(model_obj):
    current_app.session.add(model_obj)
    current_app.session.commit()
    return model_obj


def delete(model_obj) -> None:
    current_app.session.delete(model_obj)
    current_app.session.commit()
