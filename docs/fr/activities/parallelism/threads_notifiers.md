# Notifications en parallèle

Cet exercice reprend [l'exercice sur le pattern registery des décorateurs](../decorators/decorators_4.md).

**Important** : Consultez [la page d'index](index.md) pour une information sur les logs.

Vous allez commencer par modifier les fonctions de *notification*. Vous avez à disposition un module 
qui simule un service de notification : `pylib.utils.notifiers`. Ce service contient une fonction 
`make_notify(service_name:str)` qui retourne une fonction. Cette fonction va simuler de manière plus 
réaliste l'envoi d'une notification en *prenant du temps*.

Commencez par modifier les fonctions "notify" en remplaçant l'affichage par un appel à cette 
fonction. Utiliser en paramètre un texte décrivant le type de service (mail, SMS…).
 
Vos fonctions doivent ressembler à :

```python
import pylib.utils.notifiers as nf


def notify_mail():
    nf.make_notify("mail")()


def notify_sms():
    nf.make_notify("SMS")()
```

Et elles sont évidemment décorées.

## Exercice

Exécutez votre code pour observer que l'envoi de notifications prend du temps.

Modifiez la fonction `send_notifications()` pour envoyer des notifications en parallèle. Vous êtes 
libres de choisir la manière de faire sur la base du contenu de la formation.

Vous pouvez commencer par la version simple puis la version avec niveaux d'alerte.
