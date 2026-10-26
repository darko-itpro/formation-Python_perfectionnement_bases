# Notifications en parallèle

Cet exercice reprend [l'exercice sur le pattern registery des décorateurs](../decorators/decorators_4.md). 
Vous pouvez donc gérer cet exercice soit comme vous l'avez découvert à l'aide de fonctions soit à 
l'aide d'un objet de gestion de notifications.

**Important** : Consultez [la page d'index](index.md) pour une information sur les logs.

## Contexte

Pour cet exercice, nous allons utiliser des fonctions de *notification*. Vous avez à disposition un 
module qui simule un service de notification : `pylib.utils.notifiers`. Ce service contient une fonction 
`make_notify(service_name:str)` qui retourne une fonction. Cette fonction va simuler de manière plus 
réaliste l'envoi d'une notification en *prenant du temps*.

Pour cela, utilisez les fonctions "notify" suivantes. Utilisez en paramètre un texte décrivant le 
type de service (mail, SMS…). Et ajoutez en évidemment d'autres.

```python
import pylib.utils.notifiers as nf


def notify_mail():
    nf.make_notify("mail")()

    
def notify_sms():
    nf.make_notify("SMS")()
```

Comme pour l'exercice précédent, vous devrez décorer ces fonctions.

## Exercice

Exécutez votre code pour observer que l'envoi de notifications prend du temps.

Modifiez la fonction `send_notifications()` pour envoyer des notifications en parallèle. Vous êtes 
libres de choisir la manière de faire sur la base du contenu de la formation.

Vous pouvez commencer par la version simple puis la version avec niveaux d'alerte.
