
notifications = []

def notify(func):
    notifications.append(func)
    return func

@notify()
def notice1():
    print("first notice")

def notice2():
    print("second notice")

@notify
def notice3():
    print("third notice")

def send_notices():
    for notification in notifications:
        notification()

send_notices()
send_notices()
