from typing import Any

from flask import current_app
from sqlalchemy import insert, update

from my_wallet.blueprints.user.models.user import User


def create_user(email: str, mobile: str, first_name: str, last_name: str) -> User:
    with current_app.sessionmaker.begin() as session:
        return session.execute(
            insert(User).values([{
                "email": email,
                "mobile": mobile,
                "first_name": first_name,
                "last_name": last_name,
            }]).returning(User)
        ).fetchone()


def update_user(user_id: int, **kwargs_to_update: Any) -> None:
    with current_app.sessionmaker.begin() as session:
        return session.execute(
            update(User).where(User.id == user_id).values(**kwargs_to_update)
        )
