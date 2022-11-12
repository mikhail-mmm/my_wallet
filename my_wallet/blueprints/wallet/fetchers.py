from flask import current_app
from sqlalchemy import select, or_

from my_wallet.blueprints.user.models import User
from my_wallet.blueprints.wallet.models import Wallet, Transaction


def fetch_wallets_for(user: User) -> list[Wallet]:
    wallets = current_app.session.execute(
        select(Wallet).where(
            or_(
                Wallet.owned_by_user_id == user.id,
                Wallet.users_with_access.any(User.id == user.id)
            )
        )
    ).fetchall()
    return [w[0] for w in wallets]


def get_wallet_by(wallet_id: int) -> Wallet | None:
    wallet_row = current_app.session.execute(
        select(Wallet).where(Wallet.id == wallet_id)
    ).fetchone()
    return wallet_row[0] if wallet_row else None


def fetch_transactions_for(wallet_id: int) -> list[Transaction]:
    transactions = current_app.session.execute(
        select(Transaction).where(Transaction.wallet_id == wallet_id)
    ).fetchall()
    return [w[0] for w in transactions]
