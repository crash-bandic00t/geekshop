from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

def send_verify_mail(user):
    verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
    subject = 'Email Confirm'
    message = f"""
        Для подтверждения учетной записи {user.username}
        на портале {settings.DOMAIN_NAME} перейдите по ссылке:
        http://localhost:8000{verify_link}
    """
    send_mail(subject, message, "noreply@localhost", [user.email])