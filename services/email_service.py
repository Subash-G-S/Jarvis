import os
import yagmail

from dotenv import load_dotenv

load_dotenv()


def send_email(
    recipient,
    subject,
    body,
    attachment=None
):

    yag = yagmail.SMTP(
        os.getenv(
            "EMAIL_ADDRESS"
        ),
        os.getenv(
            "EMAIL_APP_PASSWORD"
        )
    )

    yag.send(
        to=recipient,
        subject=subject,
        contents=body,
        attachments=attachment
    )

    return "Email sent."