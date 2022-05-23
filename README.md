# myProject
 Projet SIM
Notre projet sert a  avoir les informations des actions sur le marché.
Après avoir cherché le nom ou le symbol d'une action, vous pouvez voir les graphiques.
Vous pouvez avoir les informations selon par jour, par semaine ou par mois.
Vous pouvez survoler votre souris sur le graphique pour avoir des informations plus précises sur l'action.

Pour démarrer le site, il faut tout d'abord s'assurer si vous êtes dans le fichier my site où il y a 
le file manage.py (entrer la commande: cd mysite si nécessaire)
Ensuite, pour démarrer le site, entrer la commande: python manage.py migrate
pour migrer la base de donnée.
Enfin, vous pouvez entrer la commande: python manage.py runserver
pour démarrer votre site.
Vous pouvez aller dans un navigateur et entrer dans le site avec l'addresse 127.0.0.1:8000/home/
Vous pouvez ensuite naviguer sur le site en cliquant les boutons et en survolant.

Pour chercher, aller sur la page actions, et entrer le symbole ou le nom de l'action que vous désirer voir.
Après, dans la page de recherche, choisir la compagnie voulue.
Voir le graphique (par jour, par semaine ou par mois).

Si vous voulez, vous pouvez créer un compte aussi.
Cependant, les comptes ne servent pas à grand chose présentement.
Pour commencer, il faut créer un superuser (ou un administrateur).
Si ce n'est pas encore fait, faire: python manage.py migrate (dans le dossier mysite et
si ce n'est pas encore fait aussi, faire la commande: cd mysite pour rentrer)
Ensuite, entrer la commande python manage.py createsuperuser pour créer un admin
Entrer les informations voulus (comme mots de passe et nom)
Avec le admin, vous pouvez gérer les autres comptes plus tard (comme supprimer un compte).
Ensuite, vous pouvez rentrer dans le site et créer un compte.
Le boutton pour se connecter ou créer un compte se situe en haut à droite qui est écrit: Logout en noir
Cliquer dessus pour se connecter ou créer un compte (mettre les informations)
Vous allez voir Hello, votre nom en haut à droite dans la plupart des pages.
Pour ce déconnecter, cliquer sur le Logout.