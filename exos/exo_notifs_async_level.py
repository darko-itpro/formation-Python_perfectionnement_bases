"""
Note : consultez le sujet pour des précisions sur cet exercice
"""

import asyncio

import pylib.utils.notifiers as nf

notifications = []

def register(_func=None, *, level=1):
    def inner_register(func):
        notifications.append((level, func()))
        return func

    if _func is None:
        return inner_register
    else:
        return inner_register(_func)


@register
async def notify_mail():
    await nf.make_async_notify("mail")()

@register(level=1)
async def notify_push():
    await nf.make_async_notify("PUSH")()

@register(level=2)
async def notify_sms():
    await nf.make_async_notify("SMS")()


def notify(level=1):
    async def notifier():
        await asyncio.gather(*[notification
                               for notif_level, notification in notifications
                               if notif_level>= level])

    asyncio.run(notifier())

notify()
