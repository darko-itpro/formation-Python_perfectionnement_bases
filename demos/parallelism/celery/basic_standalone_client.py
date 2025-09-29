"""
Ce scripte envoie des tâches à Celery avec un couplage faible car ignore le code des tâches.
"""

from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

CELERY_BROKER_URL = 'pyamqp://guest:guest@127.0.0.1:5672//'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

app = Celery('tasks', backend=CELERY_RESULT_BACKEND)


for tik in range(50):
    app.send_task("send_mail", args=(f"message {tik}",), retries=True)

# Final code for task answer capturing.
task = app.send_task("send_mail", args=("Last message",), retries=True)
print(task.get())