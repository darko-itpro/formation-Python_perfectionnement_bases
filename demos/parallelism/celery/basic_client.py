from demos.parallelism.celery.basic_tasks import send_mail

for tik in range(50):
    send_mail.delay(f"message {tik}")
