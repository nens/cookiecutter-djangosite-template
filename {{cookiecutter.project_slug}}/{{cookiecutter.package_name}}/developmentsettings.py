# (c) Nelen & Schuurmans.  Proprietary, see LICENSE file.
from {{ cookiecutter.package_name }}.settings import *

DEBUG = True

LOGGING['loggers']['']['level'] = 'DEBUG'
RAVEN_CONFIG = {}

DATABASES = {
    'default': {
        'NAME': '{{ cookiecutter.package_name }}',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'buildout',
        'PASSWORD': 'buildout',
        'HOST': 'db',  # 'db' is the postgres docker name
        'PORT': 5432,
    }
}

try:
    from {{ cookiecutter.package_name }}.localsettings import *
    # For local dev overrides.
except ImportError:
    pass
