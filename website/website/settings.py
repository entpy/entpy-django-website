"""
Django settings for website project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_DIR = os.path.dirname(__file__)

PROJECT_NAME = 'website'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rlkw#_emt=s1ndhpsl$*l8duckx@784zde15&&v!^ta)xx6oni'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #True | False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
	'entpy.com',
]

"""
# debug mode settings
if (DEBUG == True):
	TEMPLATE_DEBUG = True
	ALLOWED_HOSTS = []

	STATICFILES_FINDERS = (
		'django.contrib.staticfiles.finders.FileSystemFinder',
		'django.contrib.staticfiles.finders.AppDirectoriesFinder',
		#'django.contrib.staticfiles.finders.DefaultStorageFinder',
	)

	INSTALLED_APPS = (
		'django.contrib.staticfiles',
	)
"""

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = PROJECT_NAME + '.urls'

WSGI_APPLICATION = PROJECT_NAME + '.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'it-it'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Template

# Current template name
TEMPLATE_NAME = 'blue'

# Template directory path
TEMPLATE_DIRS = [os.path.join(BASE_DIR, PROJECT_NAME + '/templates/' + TEMPLATE_NAME + '/')]

# Static file directory path
STATICFILES_DIRS = ( 
    os.path.join(PROJECT_DIR, '../project_static/' + TEMPLATE_NAME),
)

STATIC_ROOT = os.path.join(PROJECT_NAME, '../static_resources/' + TEMPLATE_NAME)
#STATIC_ROOT = BASE_DIR + PROJECT_NAME + '/static/' + TEMPLATE_NAME + ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
