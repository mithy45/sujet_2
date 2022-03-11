# sujet_2
## 1 Lancement du programme
Pour lancer notre jeu, exécuter le script Launcher.py.
Example:
>>> python3 Launcher.py

## 2 synopsis
Lancez-vous dans notre aventure en choisissant la classe que vous souhaitez
incarner.(Vous pouvez choisir la classe chevalier, mage ou guerrier)
- Chevalier
  - Vous vous faites téléporter hors de la ville à vous de rejoindre le château pour retourner auprès de la princesse.
- Mage
  - Engagez-vous dans l'escorte d'un marchand afin que le voyage se passe sans encombre.
- Guerrier
  - Vous êtes le plus grand guerrier de votre tribu et vous avez été rejeté par une princesse. Vous décidez de la conquérir d'une autre façon ...

## Explication code
Tous les personnages se basent sur la classe Character qui est la classe mère. 
Attributs :
- name : nom du personnage
- job : classe du personnage
- current_hp : les points de vie actuelle
- ad : attack damage
- max_hp : les points de vie max
- res : resistance
- monster : savoir si c'est un monstre
- ia : savoir si c'est un joueur

Chaque classe qui hérite de la classe Character a une méthode speech pour le scénario de la classe