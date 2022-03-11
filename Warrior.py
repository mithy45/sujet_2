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


class Warrior(Character):
    def __init__(self, name="Karim", ad=50, max_hp=100, res=0.60, monster=False, ia=False):
        super().__init__(name, "Guerrier", max_hp, ad, max_hp, res, monster, ia)

    def speech(self):
        speech = \
            """
        Aucun ne serait tarnir votre réputation, vous êtes le plus redoutable des
        Guerrier, incontestablement le plus terrifiant, et vous le savez bien ! 
        Vous êtes parti demander la main de la princesse de Kaslow et vous avez fini par
        être rejeté. D'un rage noire digne de votre tribu vous avez emporté sur vos
        épaules la princesse, Rosalie. C'est à cheval que vous comptez vous échapper. A
        peine sorti de la salle du trône, vous entendez les cris "Gaardes !" vous vous
        dépêcher ! Vous tombez nez à nez sur Faren le commandant en chef de la garde
        royale ! Vous déposez la princesse de vos épaules et vous sortez deux haches à
        une main ! L'heure du combat à sonner, "AAAAAAAAAAARRRHH" sera peut-être la
        dernière chose que vous direz !
        """
        print(speech)
        Combat(self, Knight(name="Faren", ad=90, max_hp=70, res=0.75, monster=False, ia=True)).fight()

        speech = \
            """
        Vous avez terrassé Faren, vous le savez, il n'est pas mort mais sera
        pas de suite sur pied ! Vous êtes fier !
        Vous emportez Rosalie, et sortez du chateau ! 
        Un choix s'offre à vous, courir hors de l'enceinte ou aller aux écuries...
        """
        print(speech)
        if choose("Ou allez-vous ?", ['écuries', 'sortie']) == 'écuries':
            speech = \
                """
        Vous vous empressez d'aller aux écuries, vous connaissez bien le
        chateau, vous y avez été invité plusieurs fois ! Quand vous avez devant, comme
        vous le pensiez un garde s'y tient, normalement vous auriez fait qu'une bouchée
        de lui, mais blessé et fatigué de votre combat contre Faren vous savez qu'une
        erreur pourrait vous être fatale, le soldat est déjà terrorisé, il sait que
        vous voulez un cheval... Voilà un défi qui vous mets de l'eau à la
        bouche vous souriez et faites votre cri de guerre ! AU COMBAT, Guerrier !! 
            """
            print(speech)
            Combat(self, Knight(name="Soldat", ad=40, max_hp=40, res=0.80, monster=True, ia=True)).fight()
        else:
            speech = \
                """
        Vous connaissez bien le chateau dans son ensemble, vous vous dirigez vers la
        sortie. Vous passez par entre les maisons, vous arrivez à esquivez tous les
        gardes, la princesse remue légèrement, mais rien de bien méchant pour un warrior
        de votre calibre.
        Vous arrivez au pont levis, aucun garde à l'horizon ! Ils sont tous partis
        rejoindre la cour sous ordre du roi. Quelle veine !
        Vous continuez à courir, ce n'est que vers la fin du village que vous vous
        retournez, et constater un garde à cheval vous rattraper ! 
        Vous savez que vous ne pourrez pas gagner le combat sans le faire descendre en
        premier. Vous vous dites nécessaire de prendre le premier coup pour pouvoir le
        faire descendre de sa monture ! Que la bataille commence !!
            """
            print(speech)
            Combat(Knight(name="Soldat", ad=40, max_hp=40, res=0.80, monster=True, ia=True), self).fight()

        speech = \
            """
        Non sans mal, vous arrivez à vous éloignez suffisamment du château ! Vous vous
        rapprochez de votre tribu, plus que quelques kilomètres et vous y êtes ! 
        Un choix s'offre à vous, continuer de dépassez vos limites ou prendre un léger
        repos ici.
        """
        print(speech)

        if choose("Qu'allez vous faire ?", ['reposer', 'continuer']) == 'reposer':
            speech = \
                """
        Vous décidez de vous reposer, vous attachez la princesse pas loin, et faites un
        petit somme. 
            """
            print(speech)
            self.restore_hp(30)
            speech = \
                """
        C'est sous un hurlement d'un homme que vous vous réveillez ! Vous ouvrez les
        yeux... Un garde fonce sur vous ! Heureusement vous dormez l'arme en main ! C'est
        reparti !! 
            """
            print(speech)
            Combat(Knight(name="Soldat", ad=40, max_hp=50, res=0.80, monster=True, ia=True), self).fight()

            speech = \
                f"""
        Vous vous en sortez ! Ouf ! Les gardes peuvent être là à tout moment ! Vous
        repartez dans votre fuite ! 
        Vous arrivez maintenant à votre tribus, le chef, votre père vous accueil, à bras
        ouvert.
        Votre conquête est réussite !! 
        Bien joue {self.name} !
            """
            print(speech)
        else:
            speech = \
                """
        Vous décidez de dépasser vos limites, vous n'êtes pas le meilleur Guerrier du
        royaume pour rien, vous courez, courez, pendant encore une longue heure, la
        princesse elle même fatiguée de cette journée s'est endormie sur vous !
        Quand vous arrivez enfin à votre tribu, le chef, votre père, vous attendent, vous
        vous écroulez de fatigue... Vous le savez, à votre réveil la suite sera encore bien riche
        en aventure....
            """
            print(speech)
