# Bot La Ferme Du Mineur (LFDM)
 
**Bot de chasse au trésor pour le serveur discord La Ferme Du Mineur**

## Fonctionnalités
On peut programmer une chasse au trésor pour plus tard dans la journée :\
On choisir l'heure à laquelle la chasse commence, le salon que le bot doit rendre accessible à tout le monde et on peut spécifier un message à envoyer au moment de l'ouveerture de la chasse au trésor.

## Les différentes commandes
`!help` = Affiche l'aide
`!ajouter` = Lance le menu pour programmer une chasse au trésor
`!liste` = Liste les chasses au trésor programmées (Pas encore fonctionnel)

## A Faire
- Voir les chasses au trésor programmées
- Supprimer une chasses au trésor programmée
- (Programmer une chasse au trésor toutes les semaines à X heure)

## Lancer le bot
Prérequis :\
- python 3.8
- Les bibliothèques `discord`, `asyncio` et `json` (installables avec la commande python -m pip install NOM_BIBLIOTHEQUE)\

Il faut remplacer `TOKEN_DE_VOTRE_BOT` par le token de votre bot dans le fichier `token.json`.\
Il faut lancer le fichier bot.py avec python dans une console ou CMD et le bot va démarrer