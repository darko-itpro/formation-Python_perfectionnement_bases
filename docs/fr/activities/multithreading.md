# MultiThreading

## Sujet : Téléchargement simulé de fichiers en parallèle

### Contexte :
Vous êtes chargé(e) de simuler le téléchargement de plusieurs fichiers à partir d’un serveur. 
Chaque téléchargement prend un temps aléatoire entre 1 et 5 secondes. Vous devez démarrer tous les 
téléchargements en même temps, et afficher un message lorsque chacun d’eux est terminé.

### Spécifications de l’exercice :

 * Créez une fonction download_file(file_name:str) :
   * Elle prend en paramètre un nom de fichier (ex : "fichier_1.txt").
   * Elle simule le téléchargement en faisant un `time.sleep()` d'une durée aléatoire entre 1 et 5 
     secondes.
   * Elle affiche un message une fois le "téléchargement" terminé.
 * Demandez à l’utilisateur combien de fichiers il veut télécharger (ou fixez une valeur par 
   défaut, ex. 5).
 * Créez un thread pour chaque téléchargement et démarrez-les tous.
 * Attendez que tous les threads soient terminés avant de terminer le programme (utilisez .join()).

### Exemple de résultat attendu :
```bash
Téléchargement de fichier_1.txt lancé...
Téléchargement de fichier_2.txt lancé...
Téléchargement de fichier_3.txt lancé...
Téléchargement de fichier_4.txt lancé...
Téléchargement de fichier_5.txt lancé...

fichier_3.txt téléchargé en 1.4 secondes
fichier_1.txt téléchargé en 2.9 secondes
fichier_5.txt téléchargé en 3.3 secondes
fichier_2.txt téléchargé en 4.7 secondes
fichier_4.txt téléchargé en 4.9 secondes
Tous les téléchargements sont terminés.
```

### Précisions

 * Commencez par une version *simple*
 * Proposez une version plus *moderne* avec `concurrent.futures.ThreadPoolExecutor`
