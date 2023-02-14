"""
Django settings for donareasy project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@yvzqm^ln_ebz$sv=cnh*^5w@=f^e6_b$nnu$(m7-vtm8pf4fx'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = config("DEBUG", default="False")

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'login',
    'baseApp',
    'Recoleccion',
    'DonacionesApp',
    'noticias',
    'ApadrinamientoApp',
    'rest_framework',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'donareasy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

WSGI_APPLICATION = 'donareasy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'donareasy',
        # 'USER': 'root',
        # 'PASSWORD': 'admin',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
        'NAME': config('MYSQL_DATABASE', default='donareasy'),
        'USER': config('MYSQL_USER', default="donareasy"),
        'PASSWORD': config('MYSQL_PASSWORD', default='admin'),
        'HOST': config('MYSQL_HOST', default="localhost"),
        'PORT': config('MYSQL_PORT', default="3306"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

#### CONFIGURACIÓN DE CORS ####
# configurar CORS_ALLOW_ALL_ORIGIN para Truepermitir que cualquier origen
# realice solicitudes
CORS_ALLOW_ALL_ORIGINS = True
# La configuración CORS_ALLOW_CREDENTIALS para Truepermitir que se envíen
# cookies junto con solicitudes de origen cruzado.
CORS_ALLOW_CREDENTIALS = True
# configurar CORS_ALLOW_ALL_ORIGIN para Truepermitir que cualquier origen
# realice solicitudes
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]
# https://testdriven.io/blog/django-spa-auth/
# # CORS_EXPOSE_HEADERSes una lista de encabezados HTTP que están expuestos al
# # navegador.
# CORS_EXPOSE_HEADERS = ['Content-Type','X-CSRFToken']


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# La paginación le permite controlar cuántos objetos por página se devuelven.
# Para habilitarlo, agregue las siguientes líneas atutorial/settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Configuración para el envío de mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'donareasy'
EMAIL_HOST_PASSWORD = 'xhkwhhrfqnupjoiw'

# Si se quiere mostrar los mails por consola, comentar todo lo anterior y usar la
# siguiente línea
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Cuando se establece en True, si la URL de solicitud no coincide con ninguno
# de los patrones en URLconf y no termina en una barra inclinada, se emite una
# redirección HTTP a la misma URL con una barra inclinada adjunta
# https://docs.djangoproject.com/en/4.1/ref/settings/#append-slash
APPEND_SLASH = True

# Ruta absoluta del sistema de archivos al directorio que contendrá los archivos
# subidos por el usuario
# https://docs.djangoproject.com/en/4.1/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  # 'data' is my media folder
MEDIA_URL = '/media/'

# # https://testdriven.io/blog/django-spa-auth/
# # La configuración CSRF_COOKIE_SAMESITEy SESSION_COOKIE_SAMESITEpara Laxnos 
# # permite enviar cookies CSRF en solicitudes externas.
# CSRF_COOKIE_SAMESITE = 'Lax'
# SESSION_COOKIE_SAMESITE = 'Lax'

# # https://testdriven.io/blog/django-spa-auth/
# # Habilitar CSRF_COOKIE_HTTPONLYy SESSION_COOKIE_HTTPONLYbloquear JavaScript
# # del lado del cliente para que no acceda a las cookies CSRF y de sesión.
# CSRF_COOKIE_HTTPONLY = True
# SESSION_COOKIE_HTTPONLY = True
