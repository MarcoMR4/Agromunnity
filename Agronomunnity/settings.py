import os
from pathlib import Path
import locale

# Establecer el separador decimal como punto
locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')

# Configuración de formato numérico de Django
USE_THOUSAND_SEPARATOR = False
DECIMAL_SEPARATOR = '.'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_6d+57_21s0x=$=e96!ze28z2di60kb3$&+kq@xbn7u2x59!ip'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
  
    'Agronomunnity',
    #PWA
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Agronomunnity.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Agronomunnity/templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Agronomunnity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#AUTH_USER_MODEL = 'Agronomunnity.Users'
MEDIA_ROOT = os.path.join(BASE_DIR, 'Agronumunnity\\media')
MEDIA_URL = '/media/'
LOGIN_URL = '/login'
STATIC_URL = '/static/'
STATICFILES_DIR = [os.path.join(BASE_DIR, 'Agronumunnity\\static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#PWA, info para descargar web progresiva 
PWA_APP_NAME = "Agromunnity"
PWA_APP_DESCRIPTION = "Web app de gestion de corte de aguacate"
PAW_APP_THEME_COLOR = "#3CB144"
PWA_APP_BACKGROUND_COLOR = "#3CB144"
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'

PWA_APP_ICONS = [
    {
        "src": "/static/assets/img/icons/avocado.png",
        "sizes": "160x160"
     }
]

PWA_APP_ICONS_APPLE = [
    {
        "src": "/static/assets/img/icons/avocado.png",
        "sizes": "160x160"
     }
]

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'serviceworker.js')

