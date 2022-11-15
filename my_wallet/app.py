from flask import Flask
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from flask_mailgun import Mailgun
from twilio.rest import Client

from my_wallet.blueprints.statistics.blueprint import statistics_blueprint
from my_wallet.blueprints.user.blueprint import user_blueprint
from my_wallet.blueprints.user.fetchers import fetch_user_by
from my_wallet.blueprints.wallet.blueprint import wallet_blueprint
from my_wallet.config import get_config
from my_wallet.utils.config import get_connection_dsn


def compose_app() -> Flask:
    app = Flask(__name__)
    app.config.update(get_config())
    app.register_blueprint(user_blueprint, url_prefix="/user")
    app.register_blueprint(wallet_blueprint, url_prefix="/wallet")
    app.register_blueprint(statistics_blueprint, url_prefix="/statistics")

    app.engine = create_engine(get_connection_dsn(app.config), echo=True, query_cache_size=0)
    app.session = scoped_session(sessionmaker(app.engine))

    app.login_manager = LoginManager()
    app.login_manager.init_app(app)
    app.login_manager.user_loader(fetch_user_by)

    app.mailgun = Mailgun()
    app.mailgun.init_app(app)

    app.twillio_client = Client(app.config["TWILLIO_SID"], app.config["TWILLIO_AUTH_TOKEN"])
    return app
