from flask import render_template
from flask_login import login_required, current_user

from my_wallet.blueprints.wallet.fetchers import fetch_wallets_for, get_wallet_by, fetch_transactions_for


@login_required
def wallets_list():
    wallets = fetch_wallets_for(current_user)
    return render_template("wallets_list.html", wallets=wallets)


@login_required
def wallet_detail(wallet_id):
    wallet = get_wallet_by(wallet_id=wallet_id)
    transactions = fetch_transactions_for(wallet_id=wallet_id)
    return render_template("wallet_detail.html", wallet=wallet, transactions=transactions)
