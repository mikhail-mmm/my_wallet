import random

from flask import current_app


def generate_email_code() -> str:
    number = random.randint(1, 9999)
    return f"{number:04d}"


def generate_sms_code() -> str:
    number = random.randint(1, 9999)
    return f"{number:04d}"


def send_verification_email(email, code) -> None:
    current_app.mailgun.send_email(**{
        "from": current_app.config["FROM_EMAIL"],
        "to": email,
        "subject": "My wallet verification code",
        "html": f"Your email verification code is {code}",
    })


def send_verification_sms(mobile, code) -> None:
    current_app.twillio_client.messages.create(
        body=f"My wallet verification code is {code}",
        from_=current_app.config["TWILLIO_FROM_NUMBER"],
        to=mobile,
    )
