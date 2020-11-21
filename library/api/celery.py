import os

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('api')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
app.autodiscover_tasks(settings.INSTALLED_APPS, related_name='tasks') 


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.task(name='send_email_task')
def send_email_task(author_name, author_email, data):
    """
    Function to send an email to the author of a book
    """

    subject = f'Hello {author_name}! We have added your book to our database'
    html_message = render_to_string('templates/mail_template.html', {**data, 'author': author_name })
    plain_message = strip_tags(html_message)
    
    send_mail(subject, 
            plain_message,
            'niljordan23@gmail.com',
            [author_email],
            fail_silently=False)
    return None    
