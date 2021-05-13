from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'jfortti',
        'PASSWORD': 'admin2021',
        'HOST': 'localhost',
        
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS=['static']
MEDIA_URL='/media/'
MEDIA_ROOT='media'