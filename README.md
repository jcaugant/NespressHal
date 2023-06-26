# NespressHal
Script d'alimentation automatique des textes intégraux aux notices au sein de l'archive ouverte HAL

# Présentation
NespressHal est un script Python permettant d'ajouter le texte intégral aux notices au sein de l'archive ouverte HAL.
Il nécessite une configuration particulière avant lancement, et le renseignement d'informations pour que l'application soit fonctionnelle.

# Configuration
Pour que l'application fonctionne, il faut veiller à avoir tout d'abord une version de Python installée sur l'ordinateur, ou éventuellement la suite Anaconda avec le notebook Jupyter (https://www.anaconda.com/download).

L'application tourne actuellement sous Python 3.8.8 et Windows 10 64 Bits, mais un notebook Jupyter convient également. Selon la version de Windows que vous avez, la version du moteur gecko de Firefox sera différente (voir ici : https://github.com/mozilla/geckodriver/releases).

Une fois la suite Anaconda ou bien votre environnement Python confìguré, il vous faut placer les fichiers nécessaires ensemble. Pour cela :
- avec Jupyter : ouvrez l'application Jupyter Notebook et une fois sur la page d'accueil, cliquez sur le bouton Upload, pour ajouter les fichiers NespressHal.ipynb, geckodriver.exe et requirements.txt
- en Python : placez les fichiers nespresshal.py, geckodriver.exe et requirements.txt dans un même dossier.

# Lancement
Quand la configuration est terminée, vous allez pouvoir lancer l'application. 
Si vous êtes sur Jupyter, vous avez juste à exécuter la première cellule pour que les librairies s'installent, redémarrer le noyau puis exécuter la seconde cellule et le programme s'exécutera.
Si vous travaillez directement sous Python, lancez votre invite de commandes puis placez-vous dans le dossier où se trouvent les fichiers téléchargés précédemment, puis tapez la commande " pip install -r requirements.txt". Cela devrait installer les librairies nécessaires à la bonne exécution du script. Une fois cela fait, lancez nespresshal.py.

Une fois lancée, l'application va vous demander 5 éléments : login Hal, Mot de passe, numéro de votre structure, l'url de votre portail et enfin le nom de l'éditeur dont vous souhaitez récupérer le texte.
Les 2 premiers éléments servent juste à vous connecter sur votre compte. A aucun moment, ils se seront collectés ou conservés.
Le numéro de structure permet de construire l'API sur laquelle se base le script, de même que le nom de l'éditeur.
Enfin, l'url du portail permet d'effectuer l'automatisation à partir du portail au sein duquel vous avez les droits.


