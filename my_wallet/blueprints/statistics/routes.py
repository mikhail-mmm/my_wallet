from flask import Blueprint

from my_wallet.blueprints.statistics.views import statistics


def configure_routes(blueprint: Blueprint) -> None:
    blueprint.add_url_rule("/", view_func=statistics, methods=["GET", "POST"])
