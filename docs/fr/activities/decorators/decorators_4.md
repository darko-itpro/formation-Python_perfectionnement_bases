# Décorateurs 4

Soit les fonctions suivantes :
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

Recopiez ce code dans un fichier source.

Ces fonctions `notifyX()` sont des fonctions d’envoi de message.

## Exercice
### Première partie
Vous allez compléter la fonction `send_notifications()` pour qu'elle déclenche l'envoi de 
notifications en exécutant des fonctions `notifyX()`. Pour cela, vous allez créer un décorateur 
afin de décorer une ou plusieurs de ces fonctions `notifyX()`. Lorsque `send_notifications()` sera 
exécuté, toutes les fonctions décorées (et uniquement celles-ci) devront être exécutées.

Indice : vous aurez certainement besoin d’une liste pour cela…

### Seconde partie
Pour cette partie, dupliquez le fichier de l'exercice si vous souhaitez le conserver car il vous 
fera perdre la partie précédente.

Le décorateur de ces fonction doit être paramétré. Le paramètre est la priorité de la notification. 
Cette priorité est représentée par un entier positif ou nul, 0 représente la priorité la plus 
faible. La fonction d'envoi qui devient `send_notifications(priority:int = 0)` doit activer toutes 
les fonction décorées par la priorité indiquée ou supérieure.