Principe de fiction intéractive
===============================
Intro
-----
L'idée est de créer une histoire dépendante des choix et actions de l'utilisateur. 
Cela correspond à un enchaînement de tableaux où l'on vous propose plusieurs solutions, vos choix
vous meneront alors vers une voie paisible, à un combat, à reculer ou encore à votre mort.
L'utilisateur choisit son nom de joueur (et éventuellement sont genre) au début et son score sera stocké dans une 
base donnée. Autrement dit ce programme sera relié a une base de donnée permettant d'appeler les différentes fonctions de 
choix, de tableaux et d'ennemis.

Tableaux d'histoire
-------------------
Le système va fonctionner sur un système "d'évènements" prédéfinis. Chaque évènement propose des choix qui vont 
permettrent d'accéder a une liste d'autre évènements. L'histoire va se dérouler comme un déplacements entre ces 
différents évènements (un peu suivant le dessin d'un arbre de probabilité). Plus concrètement, cela va demandé
d'appeler des fontions de la base de données en fonctions des réponses du joueur (variables entrées, etc...).
