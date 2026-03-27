"""
Django settings for config project.
"""

from pathlib import Path
import os
import dj_database_url
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# SECURITY
# =========================

SECRET_KEY = config('SECRET_KEY', default="django-super-secure-key-very-long-2026-agroconnect-production-ready-123456")
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# =========================
# DATABASE
# =========================

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    # Forcer l'utilisation de psycopg2-binary
    DATABASES['default']['OPTIONS'] = {'options': '-c default_transaction_isolation=serializable'}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME', default='postgres'),
            'USER': config('DB_USER', default='postgres'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST', default='localhost'),
            'PORT': config('DB_PORT', default='5432'),
            'OPTIONS': {
                'sslmode': 'require',
            },
        }
    }

# =========================
# APPLICATIONS
# =========================

INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    # 'django_filters',  # Temporairement désactivé pour Python 3.14
    # 'drf_yasg',  # Temporairement désactivé pour Python 3.14
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'users',
    'products',
]

# =========================
# MIDDLEWARE
# =========================

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# =========================
# AUTH USER MODEL
# =========================

AUTH_USER_MODEL = 'users.User'

# =========================
# INTERNATIONALIZATION
# =========================

# =========================
# DJANGO ADMIN TEMPLATES
# =========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'products/templates/admin',
        ],
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# =========================
# STATIC & MEDIA
# =========================

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# =========================
# DJANGO REST FRAMEWORK
# =========================

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        # 'django_filters.rest_framework.DjangoFilterBackend',  # Temporairement désactivé pour Python 3.14
    ),
}

# =========================
# CORS (Flutter Web)
# =========================

CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', 
    default='http://localhost:3000,http://127.0.0.1:3000,https://agroconnect-gold.vercel.app',
    cast=lambda v: [s.strip() for s in v.split(',')]
)

CORS_ALLOW_CREDENTIALS = config('CORS_ALLOW_CREDENTIALS', default=True, cast=bool)
CORS_ALLOW_ALL_ORIGINS = config('CORS_ALLOW_ALL_ORIGINS', default=False, cast=bool)

# =========================
# JWT SETTINGS
# =========================

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}
