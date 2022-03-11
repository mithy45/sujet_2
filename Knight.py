# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 10:13:02 2022

@author: gfmac
"""
from Character import Character
from Kobolt import Kobolt

class Knight(Character):
    def __init__(self, name, ad=30, max_hp=120):
        super().__init__(name, "Knight", max_hp, ad, max_hp)

    def __init__(self):
        super().__init__("Quentin", "Knight", 120, 30, 120)

    def get_damage(self, ad):
        self.current_hp -= int(ad * 0.50)
        if self.current_hp < 0:
            self.current_hp = 0

    def speech(self):
        ennemy = Kobolt()
        self.get_damage(ennemy.ad)
        self.attack(ennemy, 1000)
        speech = \
        f"""
        *combat*
        
        Ouf, vous vous en sortez, il vous reste {self.current_hp} hp, vous trouvez une pomme,vous gagnez 10 hp ! 
        
        """
        self.current_hp += 10
        print(self.current_hp)
        """
        Une eclaircit entre les arbres vous fait apercevoir le chateau du roi au loin !
        Vous decider de vous y diriger, vous laissez derriere vous des traces de votre
        passage pour vous reperer.
        
        Apres quelque temps vous trouvez un chemin, voulez-vous le suivre ?
        
        *Oui/Non*
        
        """
    if (input("Oui/Non ?") == "Non"):
        a = \
        """
        Vous decider de continuer tout droit, au bout de quelques minutes la
        lumiere se fait de plus en plus rare vous regrettez votre choix, vous decidez de
        regarder derrierre vous pour peut etre faire marche arriere... Quoi ?!
        Impossible ! Vous vous rendez compte que vos traces laissez ont disparus ! Vous
        degainez votre épée vous vous mettez aux aguets ! Tout d'un coup tout devient
        noir, vous sentez un coup de poignard dans le dos, puis dans le ventre, vous
        entendez des hurlements et des cris de plaisir.... des bandits... Vous mourrez
        lentements... Vous pensez a votre Famille... GAME OVER
        """
        print(a)
    else:
        a = \
            """Continuez tout droit vos donne des frissons, vous sentez avoir fait le
            bon choix. Vous continuez sur votre chemin, peu de temps après à la lisiere de
            la foret un bandit vous tend une embuscade ! 
            Arfff satané bandit. C'est l'heure du combat !
            
            Vous envoyez là ou ce bandit devrait etre ! en enfer !
            
            Vous sortez de la foret et voyez au loin votre chateau... Au pont levis vous voyez une
            troupes de cavalier se dirigez vers vous, vers votre foret, vous reperez au loin
            l'armure reluisante de votre commandant, vous savez au fond de vous que cette
            petite brigade et venu à votre secours, vous vous sentez sauvé ! Vous decidez de
            prendre un temps de repos sur l'arbre le plus proche. Bien joué à vous !
                    """
        print(a)
