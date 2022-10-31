import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_forget_password_mail(email, token):

    """
    Sends email with link to reset password.
    Contains unique token based on user profile object.
    """
    subject = 'Your forget password link'
    content = f"""
            Hi there,
            click on the link to reset your password
            https://rally-blog.herokuapp.com/change-password/{token}/
        """
    message = Mail(
        from_email='robrowno@icloud.com',
        to_emails=email,
        subject=subject,
        html_content=content)
    secret_key = os.environ.get("SEND_GRID_API")
    try:
        sg = SendGridAPIClient(secret_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
