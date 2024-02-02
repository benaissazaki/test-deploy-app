import time # might need to sleep when we have to many emails per seconds

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core import mail
from django.core.mail import EmailMessage
from django.conf import settings

from .models import Product, Follower


@receiver(post_save, sender=Product)
def calling_user(sender, instance, created, **kwargs):
    """
    Firing signal upon user call and sending relevant 
    data to client through consumer.
    """
    if created:
        start_time = time.time()

        followers = Follower.objects.all()
        if followers.exists():
            connection = mail.get_connection()
            connection.open()
            for follower in followers:
                email = EmailMessage(
                    'New Content!',
                    'Dear Customer\n\nWe\'ve got brand new products that may be of interest to you. Check it out! 127.0.0.1:8000', 
                    settings.EMAIL_HOST_USER,
                    [f'{follower.email}'],
                    connection=connection,
                )
                connection.send_messages([email])
            connection.close()
        
        end_time = time.time()

        print(end_time - start_time)

#TODO: there should be a batch sending method tried but an email was sent only to one user :TODO#
# @receiver(post_save, sender=Product)
# def calling_user(sender, instance, created, **kwargs):
#     """
#     Firing signal upon user call and sending relevant 
#     data to client through consumer.
#     """
#     if created:
#         start_time = time.time()

#         followers = Follower.objects.all()
#         if followers.exists():
#             email_addresses = [follower.email for follower in followers]
#             connection = mail.get_connection()
#             connection.open()
#             email = EmailMessage(
#                 'New Content!',
#                 'Dear Customer\n\nWe\'ve got brand new products that may be of interest to you. Check it out! 127.0.0.1:8000', 
#                 settings.EMAIL_HOST_USER,
#                 email_addresses,
#                 connection=connection,
#             )
#             connection.send_messages([email])
#             connection.close()
        
#         end_time = time.time()

#         print(end_time - start_time)
