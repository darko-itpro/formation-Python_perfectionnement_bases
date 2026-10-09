# Notifications Async

Cet exercice reprend [l'exercice sur le pattern registery des décorateurs](../decorators/decorators_4.md).

**Important** : Consultez [la page d'index](index.md) pour une information sur les logs.

Vous allez commencer par modifier les fonctions de *notification*. Vous avez à disposition un module 
qui simule un service de notification : `pylib.utils.notifiers`. Ce service contient une fonction 
`make_async_notify(service_name:str)` qui retourne une **coroutine**. Cette coroutine va simuler de 
manière plus réaliste l'envoi d'une notification en *prenant du temps*.

Commencez par modifier les fonctions "notify" en remplaçant l'affichage par un appel à cette 
fonction. Utiliser en paramètre un texte décrivant le type de service (mail, SMS…).
 
Vos fonctions doivent ressembler à :

```python
import pylib.utils.notifiers as nf


async def notify_mail():
    await nf.make_async_notify("mail")()


async def notify_sms():
    await nf.make_async_notify("SMS")()
```

Et elles sont évidemment décorées.

## Exercice

La fonction `send_notifications()` doit maintenant exécuter les coroutines en parallèle. Modifiez la
en conséquence.

Vous pouvez commencer par la version simple puis la version avec niveaux d'alerte.

## À propos de l'exécution avec les niveaux

Dans la version avec des niveaux d'appel, vous allez probablement créer des coroutines que 
vous n'exécuterez pas du fait de leur niveau. Vous aurez alors en fin d'exécution, pour ces 
coroutines, un warning du type:

```shell
<sys>:0: RuntimeWarning: coroutine 'notify_mail' was never awaited
```

Ce qui est normal… Cet avertissement est émis par le _garbage collector_ quand une coroutine a été 
créée mais jamais atteinte ou exécutée. Vous pouvez donc l'ignorer, il n'y a _rien_ à faire. 
Dans certaines situations, il faudrait les intercepter et les _fermer_, mais dans notre cas, vous 
êtes dans une situation d'exercice alors que ce type de code est destiné à être exécuté en boucle et
recevoir plusieurs appels à notifications.

Bien entendu, même dans une situation de production, une coroutine peut ne jamais être appelée à la
fermeture du programme entrainant cet avertissement. Une évolution plus propre serait donc, juste 
avant, de parcourir la liste des notifications et de les fermer.

### Si nécessaire, quelques indices…

<details>
<summary>Indice 1, la liste des notifications</summary>
La liste des notifications doit contenir des coroutines et non des fonctions.
</details>

<details>
<summary>Indice 2, contenu de `send_notifications()`</summary>
`send_notifications()` devra démarrer une boucle d'exécution. Pour cela, elle aura besoin d'une
coroutine qui devra être déclarée dans la fonction.
</details>

<details>
<summary>Indice 3, évolution avec des niveaux</summary>
Vous aurez certainement besoin de compréhension de listes.
</details>

