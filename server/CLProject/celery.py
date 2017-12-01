from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CLProject.settings')

app = Celery('CLProject')
platforms.C_FORCE_ROOT = True

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
from django.conf import settings

# app.config_from_object('django.conf:settings', namespace='CELERY_')
# app.config_from_object('django.conf:settings')
app.config_from_object('django.conf:settings', 'CELERY')
# print(help())
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))