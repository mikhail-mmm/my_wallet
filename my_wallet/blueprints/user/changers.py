from flask import current_app
from sqlalchemy import insert

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
