from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags



@shared_task
def sleepy(duration):
    sleep(duration)
    return None

    
@shared_task
def send_email_task(author, data):
    subject = f'Hello {author.name}! We have added your book to our database'
    html_message = render_to_string('mail_template.html', {**data, 'author': author.name })
    plain_message = strip_tags(html_message)
    
    send_mail(subject, 
            plain_message,
            'niljordan23@gmail.com',
            [author.email],
            fail_silently=False)
    return None