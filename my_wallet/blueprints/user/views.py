from flask import render_template, request, session, redirect, url_for
from flask_login import login_user, current_user

from my_wallet.blueprints.user.changers import create_user
from my_wallet.blueprints.user.fetchers import fetch_user_by
from my_wallet.blueprints.user.forms import RegistrationForm, RegistrationStep2Form
from my_wallet.blueprints.user.services.verification import generate_email_code, generate_sms_code, \
    send_verification_email, send_verification_sms


def register():
    form = RegistrationForm(request.form) if request.method == "POST" else RegistrationForm()
    if request.method == "POST" and form.validate():
        user = create_user(
            email=form.email.data,
            mobile=form.mobile.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
        )
        session["user_id"] = user.id
        session["email_code"] = generate_email_code()
        session["sms_code"] = generate_sms_code()
        send_verification_email(user.email, code=session["email_code"])
        send_verification_sms(user.mobile, code=session["sms_code"])
        return redirect(url_for(".verify"))
    return render_template("register_step1.html", form=form)


def verify():
    form = RegistrationStep2Form(request.form) if request.method == "POST" else RegistrationStep2Form()
    if request.method == "POST" and form.validate():
        user = fetch_user_by(session["user_id"])
        login_user(user)
        return redirect(url_for(".main"))
    return render_template("register_step2.html", form=form)


def main():
    user_name = f"{current_user.first_name} {current_user.last_name}"
    return render_template("main.html", name=user_name)
