from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship

from my_wallet.db.base import Base


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey("wallet.id"), nullable=False)
    timestamp = Column(DateTime)
    amount = Column(DECIMAL)
    currency = Column(String(length=10))
    description = Column(Text)

    wallet = relationship("Wallet")
