# (c) Nelen & Schuurmans.  Proprietary, see LICENSE file.

from {{ cookiecutter.package_name }}.settings import *

DATABASES = {
    # Changed server from production to staging
    'default': {
        'NAME': '{{ cookiecutter.package_name }}',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'todo.dbuser',
        'PASSWORD': 'todo.dbpassword',
        'HOST': 'todo.dbhost',
        'PORT': '5432',
        },
    }

# TODO: Put your real url here to configure Sentry.
# RAVEN_CONFIG = {
#     'dsn': ('http://some:hash@your.sentry.site/some_number')}

# Add your staging name here
ALLOWED_HOSTS = ['{{ cookiecutter.package_name }}.staging.lizard.net']
