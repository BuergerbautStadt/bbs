# -*- coding: utf-8 -*-
import os
from local import *

INSTALLED_APPS = (
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # other dependencies
    'rest_framework',
    'rest_framework_gis',
    'widget_tweaks',
    'markdown',
    # we build city apps
    'wbc.core',
    'wbc.region',
    'wbc.process',
    'wbc.news',
    'wbc.comments'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SITE_ROOT,'bbs/templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wbc.core.context_processors.settings'
            ],
        },
    },
]

ROOT_URLCONF = 'bbs.urls'
WSGI_APPLICATION = 'bbs.wsgi.application'
SITE_ID = 1

LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(SITE_ROOT,'media/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT,'static/')

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT,'bbs/static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

LOGIN_URL = '/login'

FEED_TITLE = "Bürger baut Stadt (Veröffentlichungen)"
FEED_DESCRIPTION = "Veröffentlichungen zu Bauvorhaben in Berlin"

TILES_URL = 'http://tiles.codefor.de/bbs-berlin/'
TILES_OPT = {
    'attribution': 'Map data &copy; 2012 OpenStreetMap contributors',
    'maxZoom': 18,
    'minZoom': 10,
    'zIndex': 0,
    'reuseTiles': 1
}

DEFAULT_VIEW = {
    'lat': 52.51,
    'lon': 13.37628,
    'zoom': 11
}

ENTITY_NAME = 'Bezirk'
ENTITY_MODEL = 'District'
