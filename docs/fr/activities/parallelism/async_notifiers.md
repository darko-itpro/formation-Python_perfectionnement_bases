# Notifications Async

Cet exercice reprend [l'exercice sur le pattern registery des décorateurs](../decorators/decorators_4.md).

**Important** : Consultez [la page d'index](index.md) pour une information sur les logs.

## Avant de commencer

Cet exercice va vous faire travailler les coroutines et `asyncio` dans un contexte qui doit vous 
être déjà familier. Le choix d'implémentation a été volontairement simplifié pour le contexte d'un
exercice. Consultez ces simplifications en fin de document.

## Contexte

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

La fonction `send_notifications()` doit maintenant exécuter les coroutines en parallèle. Modifiez-la
en conséquence.

Vous pouvez commencer par la version simple puis la version avec niveaux d'alerte. Pour cette 
dernière, consultez la partie ci-dessous sur la _simplification_ du sujet. 

## Si nécessaire, quelques indices…

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

## La _simplification_ du contexte de cet exercice

Ce sujet considère que vous êtes dans un exercice et donc que votre code et l'appel aux coroutines
ne sera exécuté qu'une seule fois. En conséquence, le sujet fonctionne. Mais elle néglige **qu'une 
coroutine est créée pour être exécutée et n'être exécutée qu'une seule fois**.

### Conséquence sur l'exercice à niveaux

Dans la version avec des niveaux d'appel, vous allez probablement créer des coroutines que 
vous n'exécuterez pas du fait de leur niveau. Vous aurez alors en fin d'exécution, pour ces 
coroutines, un warning du type :

```shell
<sys>:0: RuntimeWarning: coroutine 'notify_mail' was never awaited
```

Ce qui est normal… Cet avertissement est émis par le _garbage collector_ quand une coroutine a été 
créée mais jamais atteinte ou exécutée. Vous pouvez donc l'ignorer car il ne vous est pas demandé de
gérer cette situation. Si vous souhaitez le faire, ce n'est pas un filtre qu'il faudra réaliser mais 
un tri : les coroutines non appelées devront être fermées. Ceci nous fait sortir du cadre du sujet 
de cet exercice.

### Cette version ne permet d'une seule exécution

Une coroutine ne peut être exécutée qu'une seule fois. Pour _exécuter plusieurs fois_ une coroutine, 
elle doit être créée à chaque fois ce que ne permet pas la fonction proposée.
