from concurrent.futures import ThreadPoolExecutor
import pylib.utils.notifiers as nf

notifications = []

def register(_func=None, *, level=1):
    def deco_register(func):
        notifications.append((level, func))
        return func

    if _func is None:
        return deco_register
    else:
        return deco_register(_func)


@register(level=2)
def notify_mail():
    nf.make_notify("mail 📬")()

@register
def notify_sms():
    nf.make_notify("sms 📲")()

@register(level=1)
def notify_push():
    nf.make_notify("push ")()

def send_notifications(level:int=1):
    with ThreadPoolExecutor(max_workers=2) as executor:
        for notif_level, notifiaction in notifications:
            if notif_level >= level:
                executor.submit(notifiaction)

if __name__ == '__main__':
    send_notifications()
