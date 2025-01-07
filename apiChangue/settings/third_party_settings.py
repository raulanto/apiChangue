# third_party_settings.py
from .django_settings import *

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

]

LOCAL_APPS = [
    'blog',
]

# defino la url para que mande al admin
LOGIN_REDIRECT_URL = '/admin/'

INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
}


