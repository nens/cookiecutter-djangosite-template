# (c) Nelen & Schuurmans.  Proprietary, see LICENSE file.
from {{ cookiecutter.package_name }}.settings import *

DEBUG = True

LOGGING['loggers']['']['level'] = 'DEBUG'
LOGGING['loggers']['django.db.backends']['handlers'] = ['sqllogfile']
RAVEN_CONFIG = {}

DATABASES = {
    'default': {
        'NAME': '{{ cookiecutter.package_name }}',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'nens',
        'PASSWORD': 'nens',
        'HOST': 'db',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['localhost']

try:
    from {{ cookiecutter.package_name }}.localsettings import *
    # For local dev overrides.
except ImportError:
    pass
