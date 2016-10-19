# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

from {{ cookiecutter.package_name }}.settings import *

DATABASES = {
    # Changed server from production to staging
    'default': {
        'NAME': '{{ cookiecutter.package_name }}',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': '{{ cookiecutter.package_name }}',
        'PASSWORD': 'r_ic!i7%h+',
        'HOST': 's-web-db-00-d03.external-nens.local',
        'PORT': '5432',
        },
    }

# TODO: Put your real url here to configure Sentry.
# RAVEN_CONFIG = {
#     'dsn': ('http://some:hash@your.sentry.site/some_number')}

# TODO: add staging gauges ID here.
UI_GAUGES_SITE_ID = ''  # Staging has a separate one.

# Add your staging name here. Django 1.6+
ALLOWED_HOSTS = ['{{ cookiecutter.package_name }}.staging.lizard.net']
