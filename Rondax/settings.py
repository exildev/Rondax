#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Django settings for Rondax project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6c@o^-ugsi__qjr_*^3rq+*n9hpd_fa2qe$(jfc8jra--m%j+h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'exile_ui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'operacion',
    'formulario',
    'actividades',
    'fullcalendar',
    'supra'
]

EXILE_UI = {
    'site_title': 'Rondax',
    'site_header': 'Rondax',
    'index_title': 'Software para las rondas operativos',
    'media': {
        'logo': {
            'dashboard': '/media/web_hi_res_512.png',
            'page': '/media/ic_launcher.png',
            'login': '/media/web_hi_res_512.png'
        },
        'icons':{
            'operacion': {
                'icon': 'build',
                'groups': [
                    'Operación',
                ],
                'models': {
                    'Empresa': {'icon': 'business', 'group': 'Operación'},
                    'Ciudad': {'icon': 'location_city', 'group': 'Operación'},
                    'Planta': {'icon': 'view_carousel', 'group': 'Operación'},
                    'Unidad': {'icon': 'widgets', 'group': 'Operación'},
                    'Turno': {'icon': 'schedule', 'group': 'Operación' },
                    'Equipo': {'icon': 'build', 'group': 'Operación'},
                },
            },
            'usuarios': {
                'icon': 'person',
                'groups': [
                    'Usuarios',
                ],
                'models': {
                    'Operario': { 'icon': 'people', 'group': 'Usuarios' }
                }
            },
            'formulario': {
                'icon': 'content_paste',
                'groups': [
                    'Variables',
                    'Configuración'
                ],
                'models':{
                    'Tipo': {'icon':'settings', 'group': 'Configuración'},
                    'Formulario': {'icon':'assignment', 'group': 'Variables'},
                    'Campo': {'icon':'input', 'group':'Variables'},
                    'Registro': {'icon':'insert_comment', 'group':'Variables'},
                    'Valor': {'icon': 'settings', 'group':'Variables'},
                    'Entrada': {'icon': 'assignment_returned', 'group':'Variables'}
                }
            },
            'actividades': {
                'icon': 'directions_walk',
                'groups': [
                    'Actividades',
                    'Configuración'
                ],
                'models': {
                    'Actividad': {'icon': 'event', 'group': 'Actividades'},
                    'TipoActividad': {'icon': 'settings', 'group': 'Configuración'}
                },
                'menu-extra': [
                    {'name': 'Calendario', 'url': '/actividades/schedule/', 'icon': 'event', 'group': 'Actividades'}
                ]
            },
            'auth': {
                'icon': 'security',
                'groups': [
                    'Seguridad',
                ],
                'models': {
                    'Group': {'icon': 'people', 'group': 'Seguridad'},
                    'User': {'icon': 'person', 'group': 'Seguridad'}
                }
            },
            'logout': {
                'icon': 'exit_to_app',
            }
        }
    }
}

MENU_ORDER = [
    {
        'name': 'usuarios',
        'models': [
            'Operario',
        ]
    },
    {
        'name': 'formulario',
        'models': [
            'Tipo',
            'Formulario',
            'Campo',
            'Registro',
            'Valor',
            'Entrada',
        ]
    },
    {
        'name': 'operacion',
        'models': [
            'Empresa',
            'Ciudad',
            'Planta',
            'Unidad',
            'Turno',
            'Equipo',
        ]
    },
    {
        'name':'actividades',
        'models': [
            'Actividad',
            'TipoActividad',
        ],
        'menu-extra': [
            'Calendario'
        ]
    },
    {
        'name': 'auth',
        'models': [
            'Group',
            'User'
        ]
    },
    {
        'name': 'logout'
    }
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Rondax.urls'

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

WSGI_APPLICATION = 'Rondax.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rondax',
        'USER': 'postgres',
        'PASSWORD': 'Exile*74522547',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
