# project_settings.py
from pathlib import Path
import os
# Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Clave secreta y debug
SECRET_KEY = 'django-insecure-j%ev(_-a77!j*_@w62)y^88#nbo9ohj(%kov@&a*eq68*4q@d0'

DEBUG = True



# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Archivos estáticos
STATIC_URL = 'static/'

# defino la url para que mande al admin
LOGIN_REDIRECT_URL = '/admin/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
