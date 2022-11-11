from flask import current_app
from sqlalchemy import select

from my_wallet.blueprints.user.models.user import User


def fetch_user_by(user_id: str = None, email: str = None) -> User | None:
    where_clause = User.id == user_id if user_id else User.email == email
    return current_app.session.execute(
        select(User).where(where_clause)
    ).fetchone()[0]
