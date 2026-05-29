from concurrent.futures import ThreadPoolExecutor
from pylib.utils import notifiers

notifications = []

def register(_func=None, *, level:int=0):
    def register_func(func):
        notifications.append((level, func))
        return func

    if _func is None:
        return register_func
    else:
        return register_func(_func)

@register(level=2)
def notify_mail():
    notifiers.make_notify("mail")()

@register
def notify_sms():
    notifiers.make_notify("SMS")()

@register(level=1)
def notify_push():
    notifiers.make_notify("Push")()

def send_notifications(level=0):
    with ThreadPoolExecutor(max_workers=2) as executor:
        for notif_level, notification in notifications:
            if notif_level >= level:
                executor.submit(notification)

send_notifications()