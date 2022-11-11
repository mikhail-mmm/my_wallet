from flask import current_app
from sqlalchemy import select, or_

from my_wallet.blueprints.user.models import User
from my_wallet.blueprints.wallet.models import Wallet


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
