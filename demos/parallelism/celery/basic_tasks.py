"""
Nous utilisons Redis, la dépendance doit être installée :
```bash
pip install -U "celery[redis]"
```

Ensuite lancer Celery avec
```bash
celery -A demos.parallelism.celery.basic_tasks:app worker --concurrency=4 --loglevel=INFO
```

"""

import time
import random
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

CELERY_BROKER_URL = 'pyamqp://guest:guest@127.0.0.1:5672//'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

app = Celery('tasks', backend=CELERY_RESULT_BACKEND)

@app.task(name="send_mail")
def send_mail(content):
    time.sleep(random.randint(1, 3))
    logger.info(f'Sending: {content}')
    return f"End {content}"

