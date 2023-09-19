# NespressHal
Script d'ajout automatique des textes intégraux aux notices au sein de l'archive ouverte HAL

# Présentation
NespressHal est un script Python permettant d'ajouter le texte intégral aux notices au sein de l'archive ouverte HAL.
Il nécessite une configuration particulière avant lancement, et le renseignement d'informations pour que l'application soit fonctionnelle.
L'application a été testée sur Windows uniquement pour le moment.

# Configuration
L'application nécessite l'installation du navigateur Firefox. 
Il faut suivre ensuite l'installation de Python comme indiqué après.

# Installation
## Via l'invite de commandes Windows
1) Ouvrir l'invite de commandes Windows (vous pouvez y accéder en appuyant simultanément sur le bouton Windows + R, en entrant le terme "cmd" et en appuyant ensuite sur la touche Entrée
2) Une fois l'invite de commandes ouverte, tapez "python" puis Entrée. Vous serz inviter à installer Python sur votre poste via le Microsoft Store. Si cette étape ne fonctionne pas, il faut demander à votre service informatique d'installer manuellement Python.
3) Une fois Python installé, entrez la commande suivante : "python -m ensurepip". Cela installera le logiciel pip, qui permet de récupérer les librairies tierces dont l'application a besoin pour fonctionner.
4) Enfin, tapez la commande suivante : "pip install selenium requests bs4", pour installer les librairies nécessaires

## Via un Notebook Jupyter
A venir!

# Lancement
- Pour un lancement simple, exécutez le fichier appelé "nespresshal.cmd". Cela devrait automatiquement lancer le script Python.
- Une fois lancée, l'application va vous demander 5 éléments : login Hal, Mot de passe, numéro de votre structure, l'url de votre portail et enfin le nom de l'éditeur dont vous souhaitez récupérer le texte.
- Les 2 premiers éléments servent juste à vous connecter sur votre compte. A aucun moment, ils ne seront collectés ou conservés.
- Le numéro de structure et le nom de l'éditeur permettent de construire la requête API sur laquelle se base le script.
- Pour trouver votre numéro de structure, il faut le récupérer dans le référentiel AureHal : (https://aurehal.archives-ouvertes.fr/structure/index)
- Pour récupérer le nom de l'éditeur, vous pouvez vous baser sur cette requête API : (https://api.archives-ouvertes.fr/search/?q=*%3A*&rows=0&wt=json&indent=true&facet=true&facet.field=journalPublisher_s)
- Enfin, l'url du portail permet d'effectuer l'automatisation à partir du portail au sein duquel vous avez les droits.

# Points importants
- NespressHal est actuellement sur une version alpha, merci de me faire remonter les problèmes éventuels à julien.caugant@univ-amu.fr
- L'application perd en efficacité quand elle est utilisée "en fond" (c'est-à-dire, quand vous utilisez une autre application en même temps que le script). Il vaut mieux la lancer quand vous suivez une visio ou vous absentez, afin que les processus puissent tourner de manière optimale. Utiliser 2 écrans dont un permettant de faire tourner le script permet de l'exécuter sans dysfonctionnements.
- Enfin, le script sert uniquement à alimenter en texte intégral et ne sert pas à effectuer la curation des métadonnées renseignées. Le travail de curation et modération des administrateurs reste précieux et nécessaire!


