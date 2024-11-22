"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i%z+5vjq!bb+c(9&pz+@ngs)g54pg)wo!fyb$l=xdo)vf^0p9='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


APP_NAME = "Fomic Winner"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django_filters',
        
    "corsheaders",
    'rest_framework',
    'knox',
    'authentication',
    'account',
    'plan',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "authentication.middlewares.CheckActiveUserMiddleware"
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'authentication/templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'verceldb',
        'USER': 'default',
        'PASSWORD': 'XKqja8Uiz7cm',
        'HOST': 'ep-dawn-block-a43uc4ml-pooler.us-east-1.aws.neon.tech',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        #     'options': '-c statement_timeout=5000 -c idle_in_transaction_session_timeout=10000'
        },
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'fomic',       # Database name
#         'USER': 'pires',       # Database username
#         'PASSWORD': 'death the kid 2',  # Database password
#         'HOST': 'localhost',          # Database host, often 'localhost'
#         'PORT': '5432',               # Default PostgreSQL port
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'knox.auth.TokenAuthentication',
    ),
}
# Knox Configuration - Set token lifetime to 24 hours
REST_KNOX = {
    'TOKEN_TTL': timedelta(days=60),  # Set token expiration to 24 hours
    'AUTO_REFRESH': True,  # Optional: refresh token on every authenticated request
    'USER_SERIALIZER': 'authentication.serializers.UserSerializer',  # Optional: custom user serializer

}

AUTH_USER_MODEL = 'authentication.User'

ALLOWED_HOSTS = [
    '.vercel.app',
    '127.0.0.1',
    "localhost",
    "192.168.100.180",
    "192.168.100.130",
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://192.168.100.180:3000", 
    "http://192.168.100.180:8000",
    "http://192.168.100.130:8000",
    "http://192.168.100.130:3000",
    "https://fomic.vercel.app",
    "https://fomic-admin.vercel.app"
]


CORS_ALLOW_ALL_ORIGINS: True





EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'fomicwinner@gmail.com'
EMAIL_HOST_PASSWORD = 'oclm cjup pows btpv'
MAIL_FROM_NAME="${APP_NAME}"

# Looking to send emails in production? Check out our Email API/SMTP product!
# EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
# EMAIL_HOST_USER = 'fa4271ab962c32'
# EMAIL_HOST_PASSWORD = '22bd95a0a5a7b6'
# EMAIL_PORT = '2525'


# Define the path where log files will be stored
# LOG_DIR = Path(BASE_DIR) / 'logs'
# LOG_DIR.mkdir(exist_ok=True)  # Create the log directory if it doesn't exist

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,  # Keeps the default loggers

#     'formatters': {
#         'standard': {
#             'format': '{asctime} [{levelname}] {name} - {message}',
#             'style': '{',
#         },
#         'detailed': {
#             'format': '{asctime} [{levelname}] {name} [{pathname}:{lineno}] - {message}',
#             'style': '{',
#         },
#     },

#     'handlers': {
#         # Console handler for debugging
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard',
#         },
        
#         # File handler for general info logs
#         'info_file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': LOG_DIR / 'info.log',
#             'formatter': 'standard',
#         },
        
#         # File handler for errors
#         'error_file': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': LOG_DIR / 'error.log',
#             'formatter': 'detailed',
#         },
#     },

#     'loggers': {
#         # Default logger for the Django app
#         'django': {
#             'handlers': ['console', 'info_file', 'error_file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
        
#         # Custom logger for your application
#         'myapp': {
#             'handlers': ['console', 'info_file', 'error_file'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#     },
# }
