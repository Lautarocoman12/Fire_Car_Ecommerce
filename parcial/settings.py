"""
Django settings for parcial project.
"""

from pathlib import Path

# ============================
# Base
# ============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================
# Seguridad
# ============================
SECRET_KEY = "unsafe-dev-key-for-demo"
DEBUG = False

ALLOWED_HOSTS = [
    "fire-car-ecommerce.onrender.com",
    "localhost",
    "127.0.0.1",
]

# ============================
# Apps instaladas
# ============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app',
    'accounts',
]

# ============================
# Middleware
# ============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ============================
# URLs / Templates
# ============================
ROOT_URLCONF = 'parcial.urls'

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

WSGI_APPLICATION = 'parcial.wsgi.application'

# ============================
# Base de datos
# ============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ============================
# Validadores de contraseña
# ============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================
# Internacionalización
# ============================
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True

# ============================
# Archivos estáticos y media
# ============================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "app" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ============================
# Redirecciones login/logout
# ============================
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# ============================
# Usuario personalizado
# ============================
AUTH_USER_MODEL = 'accounts.UsuarioPersonalizado'

# ============================
# Default PK
# ============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
