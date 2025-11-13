# Decorators 4

We have the following functions:
```python
def notify_mail():
    print("notification on mail")

def notify_sms():
    print("notification on message")

def notify_push():
    print("notification on push service")

def send_notifications():
    pass
```

Copy this code into your source file.

Those functions `notifyX()` are each sending a message on a dedicated channel.

## Activity
### First part
You are going to fll the `send_notifications()` function so she triggers the sending of messages by
calling some of the `notifyX()` functions. For this, you will create a decorator and use it to
decorate one or more of those `notifyX()` functions. When `send_notifications()` will be called, 
all the decorated functions (and only the decorated functions) will be called.

Hint: you will certainly need a list for this.

### Second part
Duplicate your source file if you want to keep your first part.

The decorator must be parametrized. The parameter is the *priority* of the notification. The 
priority is a positive or null integer, 0 being the lowest priority. Your called function becomes 
`send_notifications(priority:int = 0)` and must activate all the functions decorated with a 
priority higher or equal to the argument.
