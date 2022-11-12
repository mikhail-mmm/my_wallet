from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from my_wallet.blueprints.wallet.changers import delete
from my_wallet.blueprints.wallet.fetchers import fetch_wallets_for, get_wallet_by, fetch_transactions_for, \
    get_transaction_by


@login_required
def wallets_list():
    wallets = fetch_wallets_for(current_user)
    return render_template("wallets_list.html", wallets=wallets)


@login_required
def wallet_detail(wallet_id):
    wallet = get_wallet_by(wallet_id=wallet_id)
    transactions = fetch_transactions_for(wallet_id=wallet_id)
    return render_template("wallet_detail.html", wallet=wallet, transactions=transactions)


@login_required
def transaction_delete(transaction_id):
    transaction = get_transaction_by(transaction_id)
    if transaction is None:
        flash("Transaction not found")
    elif transaction.wallet.owner == current_user:
        delete(transaction)
        flash("Transaction deleted")
    else:
        flash("Permission error")
    return redirect(url_for(".wallet_detail", wallet_id=transaction.wallet_id))
