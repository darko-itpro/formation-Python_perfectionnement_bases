# Le multiprocessing

Les exemples sont dans le package `demos.parallelism.multipro`.

## Illustration du multiprocessing
Le script `01_process.py` illustre le multiprocessing. Le script exécute d'abord les appels de 
manière séquentielle puis les *tâches* (`import as Task`).

Réaliser les appels :

```shell
python -m demos.parallelism.multipro.01_process
python -m demos.parallelism.multipro.01_process -p
```

Le premier exécute des threads, le second des process.

## Shared Memory
Les différents scripts `shared_memory` illustrent l'utilisation et le comportement de la mémoire
partagée.

 * `shared_memory_01.py` : principe de base de l'objet `SharedMemory`.
 * `shared_memory_02.py` : Usage de la `SharedMemory` avec un process et passage par argument.
 * `shared_memory_03.py` : Usage de la `SharedMemory` avec un process et accès par identifiant.
 * `shared_memory_04_int.py` : Usage de la SharedMemory avec liste d'entiers.
 * `shared_memory_05_sharedlist.py` :
