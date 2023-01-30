from pathlib import Path
from backend.psw import secret_key, client_id, client_secret  # импорт секретного ключа
from .settings_db import DATABASES      # импорт данных для "базы данных"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '80.78.244.196', 'reckoning.ru', 'localhost']
INTERNAL_IPS = ('127.0.0.1', '80.78.244.196', 'reckoning.ru', 'localhost')   # кортеж с перечнем IP-адресов, с которых может вестись разработка.


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django.contrib.humanize',
] + [
    'appmain.apps.AppmainConfig',
    'oauth2mailru.apps.Oauth2MailruConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # Набор панелей, появляющихся на странице в режиме отладки
    'backend.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'    # URL для шаблонов
STATICFILES_DIRS = [
    BASE_DIR / 'static',    # "Поисковики" статики. Ищет статику в STATICFILES_DIRS.
]

MEDIA_URL = '/media/'
MEDIA_ROOT = [
    BASE_DIR / 'media',    # Абсолютный путь в файловой системе, с каталогом, где файлы, загруженные пользователями.
]


# Для авторизаций и аутентификаций
LOGIN_URL = 'auth:login'
LOGIN_REDIRECT_URL = 'auth:logout'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'oauth2mailru.backends.MailRuBackend',
)

OAUTH_MAIL_RU_CLIENT_ID = client_id
OAUTH_MAIL_RU_CLIENT_SECRET = client_secret
OAUTH_MAIL_RU_REDIRECT_URI = 'http://reckoning.ru/auth/mailru/'

LOGO_NAME = "Ре-Форма"

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'