from flask import Blueprint

from my_wallet.blueprints.wallet.views.private import wallets_list, wallet_detail, transaction_delete, transaction_add,\
    wallet_add, wallet_delete, wallet_access, wallet_access_remove
from my_wallet.blueprints.wallet.views.public import api_wallets, api_wallet, api_transactions, api_transaction


def configure_routes(blueprint: Blueprint) -> None:
    blueprint.add_url_rule("/", view_func=wallets_list, methods=["GET"])
    blueprint.add_url_rule("/new", view_func=wallet_add, methods=["GET", "POST"])
    blueprint.add_url_rule("/<int:wallet_id>", view_func=wallet_detail, methods=["GET"])
    blueprint.add_url_rule("/<int:wallet_id>/delete", view_func=wallet_delete, methods=["POST"])
    blueprint.add_url_rule("/<int:wallet_id>/access", view_func=wallet_access, methods=["GET", "POST"])
    blueprint.add_url_rule(
        "/<int:wallet_id>/access/<int:user_id>/remove",
        view_func=wallet_access_remove,
        methods=["POST"],
    )

    blueprint.add_url_rule("/<int:wallet_id>/transaction/add", view_func=transaction_add, methods=["GET", "POST"])
    blueprint.add_url_rule("/transaction/<int:transaction_id>/delete", view_func=transaction_delete, methods=["POST"])

    # public API
    blueprint.add_url_rule("/api/wallets", view_func=api_wallets, methods=["GET", "POST"])
    blueprint.add_url_rule("/api/wallet/<int:wallet_id>", view_func=api_wallet, methods=["GET", "PUT", "DELETE"])
    blueprint.add_url_rule(
        "/api/wallet/<int:wallet_id>/transactions",
        view_func=api_transactions,
        methods=["GET", "POST"],
    )
    blueprint.add_url_rule(
        "/api/wallet/<int:wallet_id>/transaction/<int:transaction_id>",
        view_func=api_transaction,
        methods=["GET", "PUT", "DELETE"],
    )
