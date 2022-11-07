from flask import Flask

from my_wallet.blueprints.user.blueprint import user_blueprint
from my_wallet.config import get_config


def compose_app() -> Flask:
    app = Flask(__name__)
    app.config.update(get_config())
    app.register_blueprint(user_blueprint)
    return app
