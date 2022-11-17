from wtforms import Form, DateField, SelectMultipleField, SelectField
from wtforms.validators import InputRequired

from my_wallet.blueprints.statistics.enums import StatReportType, ReportDisplayFormat


class StatReportForm(Form):
    date_from = DateField("Date from", [InputRequired()])
    date_to = DateField("Date to", [InputRequired()])
    wallets = SelectMultipleField("Wallets", [InputRequired()])
    report_type = SelectField("Report type", [InputRequired()], choices=StatReportType.choices())
    output_format = SelectField(
        "Display format",
        [InputRequired()],
        choices=ReportDisplayFormat.choices(),
        default=ReportDisplayFormat.HTML,
    )

    def validate(self, extra_validators=None):
        if self.date_to.data < self.date_from.data:
            self.date_to.errors = f"Should be after {self.date_from.data}",
            return False
        return super().validate(extra_validators)
