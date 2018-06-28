# (c) Nelen & Schuurmans.  Proprietary, see LICENSE file.
# Base Django settings, suitable for production.
# Imported (and partly overridden) by developmentsettings.py which also
# imports localsettings.py (which isn't stored in svn).  Buildout takes care
# of using the correct one.
# So: "DEBUG = TRUE" goes into developmentsettings.py and per-developer
# database ports go into localsettings.py.  May your hear turn purple if you
# ever put personal settings into this file or into developmentsettings.py!

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# In older projects, this setting is called BUILDOUT_DIR
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Set up logging. No console logging. By default, var/log/django.log and
# sentry at 'WARN' level.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(name)s %(levelname)s\n    %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'logfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'var', 'log', 'django.log'),
        },
        'sqllogfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'var', 'log', 'sql.log'),
        },
        'sentry': {
            'level': 'WARN',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'logfile', 'sentry'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': ['null'],
            # Quiet by default! You can set it to ``['sqllogfile']``, which is
            # done in the development settings.
            'propagate': False,
            'level': 'DEBUG',
        },
        'factory': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',  # Suppress the huge output in tests
        },
        'django.request': {
            'handlers': ['console', 'logfile', 'sentry'],
            'propagate': False,
            'level': 'ERROR',  # WARN also shows 404 errors
        },
    }
}

# Production, so DEBUG is False. developmentsettings.py sets it to True.
DEBUG = False

# TODO: Switch this to the real production database.
# ^^^ 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
# In case of geodatabase, prepend with: django.contrib.gis.db.backends.(postgis)
DATABASES = {
    'default': {
        'NAME': '{{ cookiecutter.package_name }}',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': '{{ cookiecutter.package_name }}',
        'PASSWORD': 'todo.dbpassword',
        'HOST': 'todo.dbhost',
        'PORT': '5432',
        }
    }

WSGI_APPLICATION = '{{ cookiecutter.package_name }}.wsgi.application'

# Almost always set to 1.  Django allows multiple sites in one database.
SITE_ID = 1

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name although not all
# choices may be available on all operating systems.  If running in a Windows
# environment this must be set to the same as your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl-NL'
# For at-runtime language switching.  Note: they're shown in reverse order in
# the interface!
LANGUAGES = (
#    ('en', 'English'),
    ('nl', 'Nederlands'),
)
# If you set this to False, Django will make some optimizations so as not to
# load the internationalization machinery.
USE_I18N = True

USE_L10N = True

USE_TZ = True

# Absolute path to the directory that holds user-uploaded media.
MEDIA_ROOT = os.path.join(BASE_DIR, 'var', 'media')
# Absolute path to the directory where
# "python manage.py collectstatic" places all collected static files from all
# applications' /media directory.
STATIC_ROOT = os.path.join(BASE_DIR, 'var', 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
MEDIA_URL = '/media/'
# URL for the per-application /media static files collected by
# django-staticfiles.
STATIC_URL = '/static_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i@mq5&hw$tw*=+)u$&i62mflg80=q%s#fr@$exb0jfo@(lg%to'

ROOT_URLCONF = '{{ cookiecutter.package_name }}.urls'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

CACHES = {
    'default': {
        'KEY_PREFIX': BASE_DIR,
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    # Below is the default list, don't modify it.
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

INSTALLED_APPS = (
    '{{ cookiecutter.package_name }}',
    'raven.contrib.django.raven_compat',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'gunicorn',
)

# TODO: Put your real url here to configure Sentry.
# RAVEN_CONFIG = {
#     'dsn': ('http://some:hash@your.sentry.site/some_number')}

# Add your production name here
ALLOWED_HOSTS = ['{{ cookiecutter.package_name }}.lizard.net']

try:
    from {{ cookiecutter.package_name }}.localproductionsettings import *
    # For local production overrides (DB passwords, for instance)
except ImportError:
    pass
