


from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings 
import os

def send_forget_password_mail(email , token ):
    subject = 'Your forget password link'
    content = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/'
    message = Mail(
    from_email='',
    to_emails=email,
    subject=subject,
    html_content=content)
    SECRET_KEY = os.environ.get("SEND_GRID_API")
    print(SECRET_KEY)
    try:
        sg = SendGridAPIClient(SECRET_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)