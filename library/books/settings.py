SECRET_KEY = '72fslo=0lyqzsx)l&@9y*k4@!$!rp80f!^2+p9ru1%t!k%5gch'

STATIC_URL = '/static/'


CELERY_BROKER_URL = 'redis://:p7dd595a7e3a9ad5fb15007c5ddece7a3fe5ccff7faaab3f5cb53ea04acd24eb8@ec2-23-23-239-128.compute-1.amazonaws.com:26839'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'niljordan23@gmail.com'
EMAIL_HOST_PASSWORD = 'tgmkmutgcknbsrlp'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True