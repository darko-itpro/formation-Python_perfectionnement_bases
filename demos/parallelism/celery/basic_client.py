"""
Ce scripte envoie des tâches à Celery mais avec un couplage fort avec le code des tâches.
"""

from demos.parallelism.celery.basic_tasks import send_mail

for tik in range(50):
    send_mail.delay(f"message {tik}")
