"""
Django settings for CLProject project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""


import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(1, os.path.dirname(BASE_DIR))
# sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(2, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pylxp0ba2i-x6f5+)-oj*4)^moqp8x-r1c*os_gr)vega!msx&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'xadmin',
    'rest_framework',
    # 'djcelery',
    # 'django_celery_results',
    # 'celerydemo',
    'book',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CLProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'CLProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    'default': {
        # 数据库引擎
        'ENGINE': 'django.db.backends.mysql',
        # 数据库名
        'NAME': 'cl',
        # 用户名
        'USER': 'cl',
        # 密码
        'PASSWORD': '1cl.23',
        # 安装mysql数据库的主机ip
        'HOST': '123.206.210.196',
        'OPTIONS': {
            'autocommit': True,
            'init_command': 'SET default_storage_engine=INNODB',
            "charset": "utf8mb4",

        },
    }
}




# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#设置时区
LANGUAGE_CODE = 'zh-hans'  #中文支持，django1.8以后支持；1.8以前是zh-cn
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True
USE_L10N = True

USE_TZ = False   #默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static").replace('\\', '/')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media").replace('\\', '/')

REDIS_HOST = '123.206.210.196'
REDIS_PORT = '6379'
REDIS_DB_CACHE = '1'
REDIS_DB_CELERY = '2'
REDIS_DB_ARTICLE = '3'
REDIS_PASSWD = 'f886Yjhvuyfy76grhgdFYrtf'
REDIS_CONN_NOPASSWD = "redis://%s:%s/%s"
REDIS_CONN_WITHPASS = "redis://:%s@%s:%s/%s"

REDIS_KEY_ARTICLE = 'article'
REDIS_KEY_ARTICLE_LIST = 'article_list'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_CONN_NOPASSWD % (REDIS_HOST, REDIS_PORT, REDIS_DB_CACHE),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_PASSWD
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
#
#
# import djcelery
# from celery.schedules import crontab
# djcelery.setup_loader()
# BROKER_URL = REDIS_CONN_WITHPASS % (REDIS_PASSWD, REDIS_HOST, REDIS_PORT, REDIS_DB_CELERY)
# # BROKER_URL = 'redis://:密码@主机地址:端口号/数据库号'
# CELERY_RESULT_BACKEND = REDIS_CONN_WITHPASS % (REDIS_PASSWD, REDIS_HOST, REDIS_PORT, 3)
#
# from datetime import timedelta
#
#
# CELERYBEAT_SCHEDULE = {
#     'add-every-3-seconds': {
#         'task': 'celerydemo.tasks.test_celery',
#         # 'schedule': crontab(minute=u'40', hour=u'17',),
#         'schedule': timedelta(seconds=3),
#         'args': (16, 16)
#     },
#     'timing': {
#         'task': 'celerydemo.tasks.test_multiply',
#         'schedule': crontab(minute='17-20'),
#         # 'schedule': timedelta(seconds=3),
#         'args': (2, 3)
#     },
# }
