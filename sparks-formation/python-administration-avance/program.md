# Python administration avancé

## Objectifs

- Savoir créer des outils avec Python pour l'administration système
- Connaître les modules incontournables de la bibliothèque standard pour l'administration système
- Acquérir les bonnes pratiques pour développer en Python
- Comprendre des éléments avancés de Python

## Prérequis

Connaissance des bases de Python.

## Durée

3 jours.

## Public

Administrateurs système, développeurs.

## Plan de formation

Tous les éléments du programme seront mis en place dans des travaux pratiques. La formation est très orientée pratique (80% pratique 20% théorie).

### Rappels sur les bases du langage Python

La formation débute par des rappels sur le langage autour de notions de base ou de niveau intermédiaire comme les fonctions ou la programmation orientée objet.

- Les types de données
- Les opérateurs logiques et de comparaison
- Les fonctions en Python
- Les modules, les packages et le PythonPath
- Bases de la Programmation Orientée Objet
- Les exceptions

### Fonctions d'administration système en Python

Python a une riche bibliothèque de fonctions pour l'administration système. Nous parcourons dans cette partie les éléments les plus importants.

- Modules sys, shutil et os de la librairie standard
- Manipuler des fichiers, leurs permissions
- Récupérer des variables d'environnement
- Utiliser les flux standards (stdin, stdout, stderr)

### Gestion des processus

Python, grâce principalement à son module multiprocessing, est un bon outil pour paralléliser des traitements, pour utiliser pleinement les multiples cœurs des CPUs modernes.

- Utilisation du module multiprocessing
- Présentation de la classe Process
- Manipulation des processus (os.kill, os.getpid)

### Gestion des threads

Python permet de faire travailler de manière concurrente plusieurs threads. C'est une technique très intéressante pour gagner du temps sur des opérations non limitées par le CPU (par exemple toute opération limitée par les vitesses d'entrée sortie).

- Utilisation du module threading
- Instanciation et lancement de threads
- Synchronisation (lock, rlock, semaphore...)
- Communication entre threads (event objects)

### Traitement des signaux

Les signaux sont un moyen traditionnel de communiquer entre plusieurs processus. Python a un support pour ces signaux, avec son module signal.

- Définition
- Présentation du module signal
- Intercepter un signal

### Création d'interfaces en ligne de commande

Il est très intéressant en administration système de créer des outils en ligne de commande. Ceux-ci ont un très bon rapport coût/bénéfice de développement et sont particulièrement adaptés pour l'automatisation de tâches d'administration.

- Utilisation du module argparse de la librairie standard
- Gestion de programmes à commandes multiples
- Création de contenus riches en ligne de commande avec le module rich
- Présentation de modules modernes de création d'ILC comme Click et Typer

### Éléments complémentaires d'administration système

Cette partie présente des éléments souvent requis en administration système, pour programmer des sauvegardes par exemple.

- Création d'archives
- Écriture dans une base de données
- Scheduling de tâches

### Éléments avancés de Python

Ces notions Python avancées vous permettront de rendre votre code plus performant. Améliorez vos fonctions à l’aide des décorateurs et des fermetures, anticiper la résolution de problème avec les design patterns et optimisez votre code avec les listes de compréhensions et les expressions génératrices.

- Les décorateurs
- La fermeture (closure)
- Les générateurs et les mots clefs yield et yield from
- Les compréhensions de liste, ensemble, dictionnaire et générateur
