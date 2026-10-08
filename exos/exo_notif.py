import asyncio

import pylib.utils.notifiers as nf

notifications = []

def register(func):
    notifications.append(func())
    return func

@register
async def notify_mail():
    await nf.make_async_notify("mail")()

@register
async def notify_push():
    await nf.make_async_notify("PUSH")()

@register
async def notify_sms():
    await nf.make_async_notify("SMS")()


def notify():
    async def notifier():
        await asyncio.gather(*notifications)

    asyncio.run(notifier())

notify()
