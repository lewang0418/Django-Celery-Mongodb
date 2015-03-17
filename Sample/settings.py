"""
Django settings for Sample project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from kombu import Exchange, Queue
import mongoengine


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(=wkry^_!bpmyfi4_p6o4s$urzps0%)43d9wx&yt%vdd1@^2ia'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_mongoengine',
	'djcelery',
    'BlogApp'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Sample.urls'

WSGI_APPLICATION = 'Sample.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#Mongodb
#MONGO_PORT = 27017
#MONGO_HOST = os.environ.get('MONGO_PORT_6379_TCP_ADDR', '127.0.0.1')
MONGO_DB = 'MySampleDB'
mongoengine.connect(MONGO_DB)

#Redis
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_HOST = os.environ.get('REDIS_PORT_6379_TCP_ADDR', '127.0.0.1')


#Celery
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = "UTC"

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
	Queue('default', Exchange('default'), routing_key='default'),
)

CELERY_ALWAYS_EAGER = False
CELERY_ACKS_LATE = True
CELERY_TASK_PUBLISH_RETRY = True
CELERY_DISABLE_RATE_LIMITS = False
CELERY_IGNORE_RESULT = True
CELERY_SEND_TASK_ERROR_EMAILS = False
#CELERY_RESULT_BACKEND = 'redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB)

CELERY_RESULT_BACKEND = 'mongodb://127.0.0.1:30000/'
CELERY_MONGODB_BACKEND_SETTINGS = {
	'database': 'MySampleDB',
	'taskmeta_collection': 'my_taskmeta_collection',
}

CELERY_REDIS_MAX_CONNECTIONS = 1
CELERY_TASK_RESULT_EXPIRES = 600
CELERY_TASK_SERIALIZER = "json"

CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_MAX_TASKS_PER_CHILD = 1000
CELERY_ACCEPT_CONTENT = ['application/json']




#RabbitMQ
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
#RABBIT_HOSTNAME = os.environ.get('RABBIT_PORT_5672_TCP', 'localhost:5672')

#if RABBIT_HOSTNAME.startswith('tcp://'):
#	RABBIT_HOSTNAME = RABBIT_HOSTNAME.split('//')[1]

#BROKER_URL = os.environ.get('BROKER_URL', '')
#if not BROKER_URL:
#	BROKER_URL = 'amqp://{user}:{password}@{hostname}/{vhost}'.format(
#		user=os.environ.get('RABBIT_ENV_USER', 'lewang'),
#		password=os.environ.get('RABBIT_ENV_RABBITMQ_PASS', 'w0aidudu'),
#		hostname=RABBIT_HOSTNAME,
#		vhost=os.environ.get('RABBIT_ENV_VHOST', 'sample'))

# We don't want to have dead connections stored on rabbitmq, so we have to negotiate using heartbeats
BROKER_HEARTBEAT = '?heartbeat=30'
if not BROKER_URL.endswith(BROKER_HEARTBEAT):
	BROKER_URL += BROKER_HEARTBEAT

BROKER_POOL_LIMIT = 1
BROKER_CONNECTION_TIMEOUT = 10
