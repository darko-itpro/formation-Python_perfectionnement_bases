from concurrent.futures import ThreadPoolExecutor

import pylib.utils.notifiers as nf


notifications = []

def register(_func=None, *, level=1):
    def inner_deco(func):
        notifications.append((level, func))

    if _func is None:
        return inner_deco
    else:
        return inner_deco(_func)


def send_notifications(level=1):
    with ThreadPoolExecutor(max_workers=2) as executor:
        for notif_level, notification in notifications:
            if notif_level >= level:
                executor.submit(notification)


@register
def notify_mail():
    nf.make_notify("mail")()

@register(level=2)
def notify_sms():
    nf.make_notify("SMS")()

@register(level=0)
def notify_push():
    nf.make_notify("PUSH")()

send_notifications()
