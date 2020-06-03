from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ktfirsttry.settings')

app = Celery('ktfirsttry')
app.config_from_object('django.conf:settings', namespace='CELERY')
#app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()

#@app.task(bind=True)
#def debug_task(self):
#    print('Request: {0!r}'.format(self.request))


#'''
#app.conf.beat_schedule = {
#    'notif': {
#        'task': 'ktfirsttime.tasks.notification',
#        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
#    },
#}
#'''