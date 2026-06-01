from celery import shared_task
from .utils.email import send_html_email

@shared_task
def send_welcome_email_task(email, username):
    send_html_email(
        subject="Welcome to Our Platform",
        template="emails/welcome_email.html",
        context={"username": username},
        to_email=email
    )

@shared_task
def add(x, y):
    return x + y
