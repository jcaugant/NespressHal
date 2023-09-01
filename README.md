# NespressHal
Script d'alimentation automatique des textes intégraux aux notices au sein de l'archive ouverte HAL

# Présentation
NespressHal est un script Python permettant d'ajouter le texte intégral aux notices au sein de l'archive ouverte HAL.
Il nécessite une configuration particulière avant lancement, et le renseignement d'informations pour que l'application soit fonctionnelle.
L'application a été testée sur Windows uniquement pour le moment.

# Configuration
Pour que l'application fonctionne, il faut veiller à avoir tout d'abord une version de Python installée sur l'ordinateur, ou éventuellement la suite Anaconda avec le notebook Jupyter (https://www.anaconda.com/download). Vous devez également avoir le navigateur Firefox installé sur le poste.

# Installation
## Via l'invite de commandes Windows

## Via un Notebook Jupyter


# Lancement
Quand la configuration est terminée, vous allez pouvoir lancer l'application. 
Si vous êtes sur Jupyter, vous avez juste à exécuter la première cellule pour que les librairies s'installent, redémarrer le noyau puis exécuter la seconde cellule et le programme s'exécutera.
Si vous travaillez directement sous Python, lancez votre invite de commandes puis placez-vous dans le dossier où se trouvent les fichiers téléchargés précédemment, puis tapez la commande " pip install -r requirements.txt". Cela devrait installer les librairies nécessaires à la bonne exécution du script. Une fois cela fait, lancez nespresshal.py.
Si l'installation des librairies tierces via le fichier "requirement.txt" ne fonctionne pas, lancez la commande suivante : "pip install requests selenium bs4"

Une fois lancée, l'application va vous demander 5 éléments : login Hal, Mot de passe, numéro de votre structure, l'url de votre portail et enfin le nom de l'éditeur dont vous souhaitez récupérer le texte.
Les 2 premiers éléments servent juste à vous connecter sur votre compte. A aucun moment, ils se seront collectés ou conservés.
Le numéro de structure permet de construire l'API sur laquelle se base le script, de même que le nom de l'éditeur.
Pour trouver votre numéro de structure, il faut le récupérer dans le référentiel AureHal : (https://aurehal.archives-ouvertes.fr/structure/index)
Pour récupérer le nom de l'éditeur, vous pouvez vous baser sur cette API : (https://api.archives-ouvertes.fr/search/?q=*%3A*&rows=0&wt=json&indent=true&facet=true&facet.field=journalPublisher_s)
Enfin, l'url du portail permet d'effectuer l'automatisation à partir du portail au sein duquel vous avez les droits.

# Points importants
- NespressHal est actuellement sur une version alpha, merci de me faire remonter les problèmes éventuels à julien.caugant@univ-amu.fr
- L'application fonctionne moins bien quand elle est utilisée "en fond". Il vaut mieux la lancer quand vous suivez une visio ou vous absentez, afin que les processus puissent tourner de manière optimale
- Enfin, le script sert uniquement à alimenter en texte intégral et ne sert pas à effectuer la curation des métadonnées renseignées. Le travail de curation et modération des administrateurs restent précieux et nécessaire!


