from flask import abort
from flask.views import MethodView
from flask_login import current_user

from my_wallet.blueprints.api.blueprint import api_blueprint
from my_wallet.blueprints.api.schemas import WalletSchema, TransactionSchema
from my_wallet.blueprints.wallet.changers import create, update, delete
from my_wallet.blueprints.wallet.fetchers import fetch_wallets_for, get_wallet_by
from my_wallet.blueprints.wallet.models import Wallet


class WalletsView(MethodView):
    @api_blueprint.response(200, WalletSchema(many=True))
    def get(self):
        wallets = fetch_wallets_for(current_user)
        return [
            WalletSchema().dump(w)
            for w in wallets
        ]

    @api_blueprint.arguments(WalletSchema)
    @api_blueprint.response(201, WalletSchema)
    def post(self, wallet_data):
        wallet = create(
            Wallet(
                title=wallet_data["title"],
                status=wallet_data["status"],
                owned_by_user_id=current_user.id,
            ),
        )
        return WalletSchema().dump(wallet)


class WalletView(MethodView):
    @api_blueprint.response(200, WalletSchema)
    def get(self, wallet_id):
        wallet = get_wallet_by(wallet_id)
        if wallet is None:
            abort(404)
        return WalletSchema().dump(wallet)

    @api_blueprint.arguments(WalletSchema)
    @api_blueprint.response(201, WalletSchema)
    def put(self, wallet_data, wallet_id):
        wallet = get_wallet_by(wallet_id)
        if wallet is None:
            abort(404)
        wallet.title = wallet_data["title"]
        wallet.status = wallet_data["status"]
        update(wallet)
        return WalletSchema().dump(wallet)

    def delete(self, wallet_id):
        wallet = get_wallet_by(wallet_id)
        if wallet is None:
            abort(404)
        delete(wallet)
        return {}


class TransactionsView(MethodView):
    @api_blueprint.response(200, TransactionSchema(many=True))
    def get(self, args):
        return []

    @api_blueprint.arguments(TransactionSchema)
    @api_blueprint.response(201, TransactionSchema)
    def post(self, new_data):
        return {}


class TransactionView(MethodView):
    @api_blueprint.response(200, TransactionSchema)
    def get(self, args):
        return []

    @api_blueprint.arguments(TransactionSchema)
    @api_blueprint.response(201, TransactionSchema)
    def put(self, new_data):
        return {}

    def delete(self, new_data):
        return {}
