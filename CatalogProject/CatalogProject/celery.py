import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CatalogProject.settings')

app = Celery('CatalogProject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'clear-database-task':
        {
            'task': 'catalog.tasks.pay_celery',
            'schedule': crontab(minute='*/1'),
        }
}
