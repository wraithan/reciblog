import os

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Chris McDonald', 'xwraithanx@gmail.com'),
    )

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'reciblog',
        'USER': 'wraithan',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
    }

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = True
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
SECRET_KEY = 'ydv&wa4j%fm@$$1yc@ie_*1rb_q#%6vyyvq6#g$bydi_3=fzcb'
FORCE_LOWERCASE_TAGS = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    )

ROOT_URLCONF = 'reciblog.urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'tagging',
    'blog',
    'recipes', 
    'south',
    )
