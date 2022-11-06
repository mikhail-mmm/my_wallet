from my_wallet.app import compose_app


if __name__ == '__main__':
    app = compose_app()
    app.run(debug=True)
