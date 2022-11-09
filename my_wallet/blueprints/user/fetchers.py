from flask import current_app
from sqlalchemy import select

from my_wallet.blueprints.user.models.user import User


def fetch_user_by(user_id: str = None, email: str = None) -> User | None:
    where_clause = User.id == user_id if user_id else User.email == email
    with current_app.sessionmaker.begin() as session:
        user_row = session.execute(
            select(User.id, User.first_name, User.last_name, User.email, User.mobile).where(where_clause)
        ).fetchone()
        return User(
            id=user_row.id,
            first_name=user_row.first_name,
            last_name=user_row.last_name,
            email=user_row.email,
            mobile=user_row.mobile,
        ) if user_row else None
