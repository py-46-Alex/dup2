from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django_rest_passwordreset.signals import reset_password_token_created
from .models import ConfirmEmailToken, User
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save
from django.core.mail import send_mail



# sender, instance, created, **kwargs
# @receiver(post_save, sender=User)
# def psv(created, **kwargs):
#     """прветствие - письмо после создания пользователя ему на указанный емейл"""
#     if created:
#         instance = (kwargs['instance'])
#         to_email = str(instance)
#         subject = 'спасибо за регистрацию       !  Тема письма ваш логин содан '
#         message = ' тут будет инормация про токен  . !  Текст письма тут будет'
#         from_email = 't77058573118@gmail.com'
#         recipient_list = [to_email, ]
#         send_mail(subject, message, from_email, recipient_list)

#
@receiver(post_save, sender=User)
def new_user_registered_signal(user_id, created, **kwargs):
    """    отправляем письмо"""
    if created:
        token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)
        subject = f"Password Reset Token for {token.user.email}"
        to_email = token.user.email
        message = f'{token.key, }'
        from_email = 't77058573118@gmail.com'
        recipient_list = [to_email, ]
        send_mail(subject, message, from_email, recipient_list)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, **kwargs):
    """Отправляем письмо с токеном для сброса пароля"""
    subject = f"Password Reset Token for {reset_password_token.user}"
    message = reset_password_token.key,
    from_email = settings.EMAIL_HOST_USER
    to_email = reset_password_token.user.email
    recipient_list = [to_email, ]
    send_mail(subject, message, from_email, recipient_list)
#
@receiver(post_save, sender=User)
def new_order_signal(user_id, **kwargs):
    """ отправяем письмо при изменении статуса заказа """
    user = User.objects.get(id=user_id)
    subject = f"Обновление статуса заказа"
    message = 'Заказ сформирован'
    from_email = settings.EMAIL_HOST_USER
    to_email = user.email
    recipient_list = [to_email, ]
    send_mail(subject, message, from_email, recipient_list)
#