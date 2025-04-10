from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-zrm37iu0xzev6ks^p#7l)r-x0wnuk%+c&gj!s)-cp-_4j$--k2'
DEBUG = True

ALLOWED_HOSTS = ['134.199.211.102', '127.0.0.1', 'localhost', 'grupofycas.online']
CSRF_TRUSTED_ORIGINS = ['https://6cbe-170-239-164-9.ngrok-free.app']

# Application definition
INSTALLED_APPS = [
    # Mis apps
        'Perfil.apps.PerfilConfig',
        'Caja.apps.CajaConfig',  # App de la caja
        'Agenda.apps.AgendaConfig', # App de la agenda
        'Mensajeria.apps.MensajeriaConfig', # App de la mensajeria
        'Maps.apps.MapsConfig', # App de los mapas
        'Calculator.apps.CalculatorConfig', # App de la calculadora
        'Credit.apps.CreditConfig', # App de los creditos
        'Client.apps.ClientConfig', # App de los clientes
        'Company.apps.CompanyConfig', # Applicacion de la empresa
        'App.apps.AppConfig', # App principal
        'Login.apps.LoginConfig', # App de login
        'Inversion.apps.InversionConfig', # App de inversion
        'Asistente.apps.AsistenteConfig', # App de asistente
        'Published.apps.PublishedConfig', # App de publicaciones, marqueting  planes y de mas.
        'Membreship.apps.MembreshipConfig',

        'paypal.standard.ipn', # Paypal

    # Django apps
        'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes',
        'django.contrib.sessions', 'django.contrib.messages',  'django.contrib.staticfiles',
        'django.contrib.humanize', 
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs
ROOT_URLCONF = 'Easy.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Easy', 'templates')],  # 📌 Agregar esta línea
        'APP_DIRS': True,  # Esto solo funciona dentro de apps, pero no en el proyecto principal
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

WSGI_APPLICATION = 'Easy.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Santo_Domingo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'Easy/Easy/static/' 
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PAYPAL_TEST = True
#PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL = 'sb-wamqy39355606@business.example.com'