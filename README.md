# Bot La Ferme Du Mineur (LFDM)
 
**Bot de chasse au trésor pour le serveur discord La Ferme Du Mineur**

## Fonctionnalités
On peut programmer une chasse au trésor pour plus tard dans la journée :\
On choisit :
- l'heure à laquelle la chasse au trésor commence
- le salon de la chasse au trésor (que le bot va rendre accessible quand la chasse commencera)
- on peut spécifier un message à envoyer au moment de l'ouverture de la chasse au trésor (sur le salon de notre choix)

## Les différentes commandes
`!help` = Affiche l'aide\
`!ajouter` = Lance le menu pour programmer une chasse au trésor\
`!liste` = Liste les chasses au trésor programmées (Pas encore fonctionnel)

## A Faire
- Voir les chasses au trésor programmées
- Supprimer une chasses au trésor programmée
- Restreindre la programmation/suppression des chasses au trésor à un certain rôle/aux personnes ayant les permissions admin
- (Programmer une chasse au trésor toutes les semaines à X heure)


## Lancer le bot
Prérequis :
- python 3.8
- Les bibliothèques `discord`, `asyncio` et `json` (installables avec la commande python -m pip install NOM_BIBLIOTHEQUE)\

Il faut remplacer `TOKEN_DE_VOTRE_BOT` par le token de votre bot dans le fichier `token.json`.\
Il faut lancer le fichier bot.py avec python dans une console ou CMD et le bot va démarrer