from flask import Flask


def compose_app() -> Flask:
    app = Flask(__name__)
    return app

