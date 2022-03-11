# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:20:12 2022

@author: Quentin Brice Théo Micka Karim François
"""
from Character import Character
from Combat import Combat
from Knight import Knight
from Kobolt import Kobolt
from utils import choose


class Mage(Character):
    def __init__(self, name="Théo", ad=80, max_hp=60, res=0.90, monster=False, ia=False):
        super().__init__(name, "Mage", max_hp, ad, max_hp, res, monster, ia)

    def speech(self):
        speech = \
            f"""
        Bonjour, grand mage {self.name} vous avez été recruté par Monsieur Borte, le marchand de bijoux, 
        pour faire l’escorte vers la plus grande ville marchande de la région pour y faire affaire avec les 
        nobles. Vous décidez de vous coucher tôt pour cette nouvelle aventure qui démarre demain matin à l’aube. 
        Après votre excellent déjeuner de pain rassis et le reste de beurre que vous avez. Vous prenez votre 
        bâton magique et vous vous retrouvez sur la place de la ville où le marchand vous attend avec sa petite 
        charrette. Vous vous retrouvez hors de la ville. Ça y est, l’aventure commence ! Vous arrivez dans une 
        forêt sombre tout à coup un petit Kobolt affamé sort d’un buisson pour vous attaquer. Le combat commence ! 
            """
        print(speech)
        Combat(self, Kobolt()).fight()

        speech = \
            """
        Vous arrivez à vous en sortir ! Monsieur Borte est rassuré de vous avoir en escorte. 
        Après cette péripétie, vous reprenez la route. Après plusieurs heures passées dans la forêt, 
        vous commencez à entrevoir le début d’une plaine. Vous vous sentez mal depuis la fin du combat. 
        Comme-ci quelque chose vous observez... Tout à coup, un Kobolt adulte vous saute dessus ! 
        """
        print(speech)
        kobolt = Kobolt()
        kobolt.attack(self)

        speech = \
            """
        Vous vous faites remarquer que c’est sûrement la mère du petit que 
        vous avez chassé quelques heures auparavant. Le combat s’engage !
        """
        print(speech)
        Combat(kobolt, self).fight()
        if kobolt.is_alive():
            speech = \
                """
        Vous arrivez à prendre la fuite avec la charrette. Après une heure de fuite, la nuit, commence à tomber. 
        Vous décidez de faire un feu de camp avec Monsieur Borte. Après une petite soupe et quelques soins,
        vous vous endormez à côté du feu… Vous entendez un hurlement à côté de vous après quelques heures de sommeil. 
        C’était la femelle kobolt qui est venue se venger. 
        Cette fois, elle n’était pas seule. Ils étaient une meute de 5 !!!! 
        Vous vous retrouvez dépassé et vous mourrez lamentablement ...
            """
            print(speech)
            return
        speech = \
            """
        Vous arrivez à vous en sortir malgré les blessures. 
        Monsieur Borte par admiration, vous offre une potion pour votre courage.
        Le réveil se fait difficile le matin, mais vous reprenez la route avec panache. 
        Vous avez déjà plus de la moitié du chemin. L’aventure se déroule sans accroche depuis ce matin. 
        Il ne vous reste plus que 2 h avant d’arriver à destination. Monsieur Borte décide de faire une pause. 
        Vous vous arrêtez donc sur le bord de chemin. Un bandit commence à courir dans votre direction ! 
        Monsieur Borte et vous décident de vite vous enfuir afin d’éviter le combat. 
        À peine le début de votre fuite, le bandit envoie sa hachette sur la charrette ce qui l’immobilise. 
        La fuite est donc impossible. Le combat est inévitable ... Le combat s’entame !
        """
        print(speech)
        Combat(self, Knight(name="Soldat", ad=30, max_hp=70, res=0.75, monster=False, ia=True)).fight()

        speech = \
            """
        Félicitations ! Vous remportez votre combat ! 
        Après le rafistolage de la charrette, vous reprenez votre route. Vous arrivez enfin à destination ! 
        Après cette dure aventure, Monsieur Borte vous donne votre récompense et vous invite dans
        l’auberge de la place pour une bière bien méritée.
        """
        print(speech)
