from flask import render_template
from flask_login import login_required, current_user

from my_wallet.blueprints.wallet.fetchers import fetch_wallets_for


@login_required
def wallets_list():
    wallets = fetch_wallets_for(current_user)
    return render_template("wallets_list.html", wallets=wallets)
