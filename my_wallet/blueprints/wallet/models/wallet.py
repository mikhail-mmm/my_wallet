from sqlalchemy import Column, Integer, String, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship

from my_wallet.blueprints.wallet.enums import WalletStatus
from my_wallet.db.base import Base


wallet_access_table = Table(
    "wallet_access",
    Base.metadata,
    Column("wallet_id", ForeignKey("wallet.id"), primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
)


class Wallet(Base):
    __tablename__ = "wallet"

    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    status = Column(Enum(WalletStatus))
    owned_by_user_id = Column(Integer, ForeignKey("user.id"), nullable=True)

    owner = relationship("user.User", back_populates="wallets")
    users_with_access = relationship("user.User", secondary=wallet_access_table)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.email})"
