from flask import current_app
from sqlalchemy import select

from my_wallet.blueprints.user.models.user import User


def fetch_user_by(user_id) -> User:
    with current_app.sessionmaker.begin() as session:
        user_row = session.execute(
            select(User.id, User.first_name, User.last_name, User.email, User.mobile).where(User.id == user_id)
        ).fetchone()
        return User(
            id=user_row.id,
            first_name=user_row.first_name,
            last_name=user_row.last_name,
            email=user_row.email,
            mobile=user_row.mobile,
        )
