READ ME
 
Ouvrir un terminal. 
Se rendre au dossier contenant le dossier projet_QUETEL et plus précisément dans quizz avec la commande :
cd le/chemin/dossier/projet_QUETEL/quizz

Créer un environnement conda : 
conda create --name djangoenv python=3.7
conda install --name djangoenv django
conda install --name djangoenv sqlparse

Ouvrir l'environnement conda :
conda activate djangoenv

Permettre le lancement de l'interface graphique : 
python manage.py runserver

Ouvrir le lien http://127.0.0.1:8000/ dans un navigateur internet. 

Lorsque l'interface web se lance vous pouvez vous connecter avec le menu latéral à gauche en cliquant sur le bouton "Login" ou alors essayer un quizz aléatoire en cliquant soit sur le bouton au milieu de la page "Try a random quizz !" ou en cliquant dans "Try a quizz" dans le menu latéral.

Dans mon cas, je n'ai pas réussi l'identification (le login) donc pour accéder au réel quizz il faut cliquer sur "Quizz" dans le menu latéral. 

Ensuite, on est dans l'interface du quizz. On peut choisir le quizz voulu "Microscopy" ou "Biological context" ou même explorer toutes les images avec leurs informations grâce au bouton "Explore the images". 
Ces actions sont aussi réalisables dans le menu latéral.

Dans le menu latéral on peut également retourner à l'accueil en cliquant sur "Home", cela peut être utile lorsqu'on est dans un quizz et que l'on veut arrêter par exemple. 
Enfin, on peut aussi se déconnecter et retourner à l'écran d'accueil principal en cliquant dans le menu latéral sur "Logout". Cette action devrait normalement déconnecter l'utilisateur mais comme je n'ai pas réussi l'identification je n'ai évidement pas pu effectuer de déconnection. 

Côté quizz en lui même, il suffit de suivre les instructions affichées. Une question s'affiche avec les images correspondantes et les réponses possibles. Il suffit de cliquer sur la réponse que l'on pense juste et un pop up de réponse s'ouvre. Il faut ensuite cliquer sur le bouton du pop up qui est soit un retour à l'accueil dans le cas du test du quizz soit une prochaine question lorsque l'utilisateur est connecté dans le réel quizz. 

Dans l'interface permettant d'explorer les images il suffit de scroller pour explorer les images et leur description. Il est aussi possible de faire des recherches spécifiques à des colonnes en passant par les recherches en bas de la page.