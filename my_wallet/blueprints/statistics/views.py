import datetime

from flask import request, render_template
from flask_login import login_required, current_user

from my_wallet.blueprints.statistics.custom_types import ReportData
from my_wallet.blueprints.statistics.forms import StatReportForm
from my_wallet.blueprints.wallet.fetchers import fetch_wallets_for


@login_required
def statistics():
    form = StatReportForm(request.form) if request.method == "POST" else StatReportForm()
    wallets = fetch_wallets_for(current_user)
    form.wallets.choices = [(str(w.id), w.title) for w in wallets]
    report_data = None
    if request.method == "POST" and form.validate():
        report_data = ReportData(
            columns=["date", "Test1", "Test2"],
            data=[
                [datetime.datetime(2022, 4, 3), 5, 1],
                [datetime.datetime(2022, 4, 3), 5, 1],
                [datetime.datetime(2022, 4, 3), 5, 1],
                [datetime.datetime(2022, 4, 3), 5, 1],
            ],
        )
    return render_template("stat_report_form.html", form=form, report_data=report_data)
