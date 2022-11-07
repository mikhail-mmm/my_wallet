from sqlalchemy import Column, Integer, String, Boolean

from my_wallet.db.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(30))
    is_email_verified = Column(Boolean)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.email})"
