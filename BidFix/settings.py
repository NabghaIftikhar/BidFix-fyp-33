"""
Django settings for BidFix project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
import os
import sys
from datetime import timedelta
from pathlib import Path
from django.core.management.utils import get_random_secret_key
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5pi8@ltq38n69yzsz#ljwmvm$(9c7@o=h4ntam$%pn0at*ycw5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_management',
    'bidding_and_transaction',
    'products',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'drf_yasg',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'BidFix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'BidFix.wsgi.application'

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd9ff492u5pbsl',
        'USER': 'ihwwyfeakwhjfg',
        'PASSWORD': '510f00b6b747e50c2c3c510315e9b5e858fdb84da43d801f7ef4ccaf0816a8fb',
        'HOST': 'ec2-34-197-84-74.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
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


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = 'staticfiles'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

#STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social_core.backends.amazon.AmazonOAuth2',
)
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}

# DJOSER = {
#     'LOGIN_FIELD': 'email',
#     'PASSWORD_RESET_CONFIRM_URL': 'api/user_management/password/reset/confirm/{uid}/{token}/',
#     'ACTIVATION_URL': 'api/user_management/activate/{uid}/{token}/',
#     'SEND_ACTIVATION_EMAIL': True,
#     'SERIALIZERS': {
#         'user': 'user_management.serializers.CustomUserSerializer',
#         'user_create': 'user_management.serializer.UserRegistrationSerializer'
#
#     },
#     'USER_CREATE_PASSWORD_RETYPE': True,
#     'SEND_CONFIRMATION_EMAIL': True,
#
# }
DJOSER = {
    'LOGIN_FIELD': 'email',
    'PASSWORD_RESET_CONFIRM_URL': 'api/user_management/password/reset/confirm/{uid}/{token}/',
    'ACTIVATION_URL': 'api/user_management/activate/{uid}/{token}/',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        # 'user': 'user_management.serializers.CustomUserSerializer',
        # 'current_user': 'user_management.serializers.CustomUserSerializer',
        'user_create': 'user_management.serializers.CreateUserSerializer',
        # 'user_create_password_retype': 'user_management.serializers.CreateUserSerializer',

    },
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SEND_CONFIRMATION_EMAIL': True,

}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'iftikharnabgha93@gmail.com'
AUTH_USER_MODEL = "user_management.User"
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '825154f4825dde'
EMAIL_HOST_PASSWORD = 'a55fa725ec41e5'
EMAIL_PORT = '2525'

# Number of seconds of inactivity before a user is marked offline

USER_ONLINE_TIMEOUT = 300

# Number of seconds that we will keep track of inactive users for before
# their last seen is removed from the cache

USER_LASTSEEN_TIMEOUT = 60 * 60 * 24 * 7
GOOGLE_MAPS_API_KEY = 'AIzaSyCZl543xTZIU0T02nd4d9l1Ie5QYADBFqQ'
