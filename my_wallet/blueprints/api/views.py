from flask.views import MethodView

from my_wallet.blueprints.api.blueprint import api_blueprint
from my_wallet.blueprints.api.schemas import WalletSchema, TransactionSchema


class WalletsView(MethodView):
    @api_blueprint.response(200, WalletSchema(many=True))
    def get(self, args):
        return []

    @api_blueprint.arguments(WalletSchema)
    @api_blueprint.response(201, WalletSchema)
    def post(self, new_data):
        return {}


class WalletView(MethodView):
    @api_blueprint.response(200, WalletSchema)
    def get(self, args):
        return []

    @api_blueprint.arguments(WalletSchema)
    @api_blueprint.response(201, WalletSchema)
    def put(self, new_data):
        return {}

    def delete(self, new_data):
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
