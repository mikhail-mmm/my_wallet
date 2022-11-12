from flask import Blueprint

from my_wallet.blueprints.wallet.views import wallets_list, wallet_detail


def configure_routes(blueprint: Blueprint) -> None:
    blueprint.add_url_rule("/", view_func=wallets_list, methods=["GET"])
    blueprint.add_url_rule("/<int:wallet_id>", view_func=wallet_detail, methods=["GET"])
