from django.core.mail import send_mail


def email(message, message2):
    messages = f'Код регистрации: \n{message2}'
    send_mail(
        'Код авторизации',
        messages,
        f'{message}',  # почта куда
        [f'{message}'],  # Это поле Кому:
        fail_silently=False,
    )
