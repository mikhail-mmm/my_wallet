from flask import Blueprint

from my_wallet.blueprints.wallet.views import wallets_list, wallet_detail, transaction_delete, transaction_add


def configure_routes(blueprint: Blueprint) -> None:
    blueprint.add_url_rule("/", view_func=wallets_list, methods=["GET"])
    blueprint.add_url_rule("/<int:wallet_id>", view_func=wallet_detail, methods=["GET"])

    blueprint.add_url_rule("/<int:wallet_id>/transaction/add", view_func=transaction_add, methods=["GET", "POST"])
    blueprint.add_url_rule("/<int:transaction_id>/delete", view_func=transaction_delete, methods=["POST"])
