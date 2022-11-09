from flask import Blueprint

from my_wallet.blueprints.user.views import register, verify, main, login, login_verify, logout


def configure_routes(blueprint: Blueprint) -> None:
    blueprint.add_url_rule("/register/", view_func=register, methods=["GET", "POST"])
    blueprint.add_url_rule("/verify/", view_func=verify, methods=["GET", "POST"])

    blueprint.add_url_rule("/login/", view_func=login, methods=["GET", "POST"])
    blueprint.add_url_rule("/login/verify/", view_func=login_verify, methods=["GET", "POST"])
    blueprint.add_url_rule("/logout/", view_func=logout, methods=["GET"])

    blueprint.add_url_rule("/", view_func=main, methods=["GET"])
