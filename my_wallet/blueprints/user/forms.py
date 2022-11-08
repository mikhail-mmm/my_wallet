from flask import current_app, session
from sqlalchemy import exists
from wtforms import Form, StringField, EmailField
from wtforms.validators import InputRequired

from my_wallet.blueprints.user.models.user import User


class RegistrationForm(Form):
    first_name = StringField('First name', [InputRequired()], render_kw={"placeholder": "First name"})
    last_name = StringField('Last name', [InputRequired()], render_kw={"placeholder": "Last name"})
    email = EmailField('Email', [InputRequired()], render_kw={"placeholder": "Email"})
    mobile = StringField('Mobile phone', [InputRequired()], render_kw={"placeholder": "Mobile"})

    def validate(self, extra_validators=None):
        with current_app.sessionmaker.begin() as session:
            is_duplicates_exists = session.query(
                exists(User).where(
                    User.email == self.email.data,
                    User.mobile == self.mobile.data
                ),
            ).scalar()
        if is_duplicates_exists:
            self.email.errors = "Please use another email/mobile pair",
            return False
        return super().validate(extra_validators)


class RegistrationStep2Form(Form):
    email_code = StringField("Email code", [InputRequired()], render_kw={"placeholder": "Email code"})
    sms_code = StringField("SMS code", [InputRequired()], render_kw={"placeholder": "SMS code"})

    def validate(self, extra_validators=None):
        all_codes_are_ok = True
        if session["email_code"] != self.email_code.data:
            self.email_code.errors = "Wrong code",
            all_codes_are_ok = False
        if session["sms_code"] != self.sms_code.data:
            self.sms_code.errors = "Wrong code",
            all_codes_are_ok = False
        if not all_codes_are_ok:
            return False
        return super().validate(extra_validators)
