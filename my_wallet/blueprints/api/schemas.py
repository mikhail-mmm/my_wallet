from marshmallow import Schema
from marshmallow.fields import Int, String, List, DateTime, Decimal


class WalletSchema(Schema):
    id = Int(dump_only=True)
    title = String()
    status = String()
    owned_by_user_id = Int()
    users_with_access = List(Int())


class TransactionSchema(Schema):
    id = Int(dump_only=True)
    wallet_id = Int(dump_only=True)
    timestamp = DateTime()
    amount = Decimal()
    currency = String()
    description = String()
