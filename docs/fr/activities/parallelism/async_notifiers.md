# Notifications Async

Cet exercice reprend [l'exercice sur le pattern registery des décorateurs](../decorators/decorators_4.md).

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

La fonction `send_notifications()` doit maintenant exécuter les coroutines en parallèle. Modifiez la
en conséquence.

Si nécessaire, quelques indices…

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

