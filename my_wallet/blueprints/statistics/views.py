from flask import request, render_template
from flask_login import login_required, current_user

from my_wallet.blueprints.statistics import report_generators
from my_wallet.blueprints.statistics.enums import StatReportType
from my_wallet.blueprints.statistics.forms import StatReportForm
from my_wallet.blueprints.wallet.fetchers import fetch_wallets_for


@login_required
def statistics():
    report_generators_map = {
        StatReportType.BIGGEST_EXPENSES: report_generators.generate_biggest_expenses_report,
        StatReportType.EXPENSES_BY_WEEKDAY: report_generators.generate_expenses_by_weekday_report,
        StatReportType.EXPENSES_BY_WEEK: report_generators.generate_expenses_by_week_report,
        StatReportType.EXPENSES_BY_TYPE: report_generators.generate_expenses_by_type_report,
        StatReportType.WEEKLY_BALANCE: report_generators.generate_weekly_balance_report,
    }
    form = StatReportForm(request.form) if request.method == "POST" else StatReportForm()
    wallets = fetch_wallets_for(current_user)
    form.wallets.choices = [(str(w.id), w.title) for w in wallets]
    report_data = None
    if request.method == "POST" and form.validate():
        wallets_ids = [int(w) for w in form.wallets.data]
        report_type = StatReportType(form.report_type.data)
        report_generator = report_generators_map[report_type]
        report_data = report_generator(
            date_from=form.date_from.data,
            date_to=form.date_to.data,
            wallets_ids=wallets_ids,
        )
    return render_template("stat_report_form.html", form=form, report_data=report_data)
