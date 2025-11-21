# Le multithreading

Les exemples sont dans le package `demos.parallelism.threads`. Certains exemples ont une version 
avec un affichage plus *riche* dans `demos.parallelism.threads_rich`.

## Le besoin de parallélisme
Le script `01_thread.py` est un exemple séquentiel destiné à illustrer la durée totale d'exécution 
de deux *tâches*. La version `demos.parallelism.threads_rich.01_thread_rich` possède un affichage 
moins chargé.

Exécutez :
```shell
python -m demos.parallelism.threads.01_thread
python -m demos.parallelism.threads_rich.01_thread_rich
```

## Les treads, les bases

* `02a_thread.py` : exemple avec des threads. La durée totale est celle du programme principal. 
  L'ajout des `.join()` permet d'attendre la finalisation des actions en parallèle.
* `demos.parallelism.threads_rich.02_thread_rich` : est le même que le précédent avec un affichage 
  moins chargé.
* `02b_custom_thread.py` : de comportement identique au précédent mais en déclarant un objet 
  thread *custom*.
* `demos.parallelism.threads_rich.02_custom_thread_rich` : version avec thread *custom* et 
  affichage plus informatif.

Exécutez :
```shell
python -m demos.parallelism.threads.02a_thread
python -m demos.parallelism.threads_rich.02_thread_rich
python -m demos.parallelism.threads.02b_custom_thread
python -m demos.parallelism.threads_rich.02_custom_thread_rich
```

Les script `02c_timer.py` est une curiosité adapté à notre cas et permet de lancer un thread après 
un délais.

## Les sémaphores
 * `03_semaphore.py` : exemple de base
 * `demos.parallelism.threads_rich.03_semaphore_rich` : affichage plus lisible.

Éxécutez :
```shell
python -m demos.parallelism.threads_rich.03_semaphore_rich
```

## Une interface plus haut niveau
Le module `concurrent.futures` fournit une interface haut niveau pour l'exécution asynchrone.

 * `04a_thread_future.py` : Reprise du second exemple avec les threads.
 * `04b_more_futures.py` : Pour aller plus loin en associant une callback aux tâches.

Exécutez :
```shell
python -m demos.parallelism.threads.04a_thread_futures
python -m demos.parallelism.threads.04b_more_futures
```

## Les verrous

 * `05a_lock.py` : Illustration du problème de concurrence.
 * `05b_lock_bank01_without.py` : exemple illustrant la concurrence avec un `ThreadPoolExecutor` 
   sans lock.
 * `05c_lock_bank02_withlock.py` : exemple illustrant la concurrence avec un `ThreadPoolExecutor` 
   avec lock.
 * `05d_lock_bank03_deadlock.py` : exemple conduisant au deadlock.

Exécutez :
```shell
python -m demos.parallelism.threads.05a_lock
python -m demos.parallelism.threads.05b_lock_bank01_without
python -m demos.parallelism.threads.05c_lock_bank02_withlock
python -m demos.parallelism.threads.05d_lock_bank03_deadlock
```

## 06_wait.py
Concurrence gérée avec la méthode `wait`.

## Les limites du multithreading
Illustration avec le script `07_limit.py`.

Exécutez :
```shell
python -m demos.parallelism.threads.07_limit
```
