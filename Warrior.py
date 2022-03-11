from Character import Character
from Kobolt import Kobolt

class Warrior(Character):
    def __init__(self, name="Karim", ad=50, max_hp=100, res=0.60):
        super().__init__(name, "Warrior", max_hp, ad, max_hp, res)

    def speech(self):
        speech = \
            f"""
        Malheureusment vous êtes fait téléporter dans la foret de Fark, là où les monstres les plus terrifiants rodent ! 
        Vous vous remettez à peine de vos esprits que vous vous faites déjà agresser par 
        un Kobolt ! Vous vous saisissez de votre arme et engagez le combat ! 
        *combat*
        """
        print(speech)
        ennemy = Kobolt()
        ennemy.attack(self)
        self.attack(ennemy)
        print(f"Il vous reste {self.current_hp}")
        speech = \
            f"""
        Ouf, vous vous en sortez, il vous reste {self.current_hp} hp, vous trouvez une pomme... 
        """
        print(speech)
        self.restore_hp(10)
        print(f"\tVous avez {self.current_hp} hp")
        speech = \
        """
        Une éclaircie entre les arbres vous fait apercevoir le château du roi au loin !
        Vous decidez de vous y diriger, vous laissez derriere vous des traces de votre
        passage pour vous repérer.

        Apres quelque temps vous trouvez un autre chemin, voulez-vous le suivre ?

        *Oui/Non*
        """
        print(speech)

        if (input("\tOui/Non ? :\n\t").lower() == "non"):
            a = \
                """
                Vous decidez de continuer tout droit, au bout de quelques minutes la
                lumiere se fait de plus en plus rare vous regrettez votre choix, vous decidez de
                regarder derrière vous pour peut-être faire marche arriere... Quoi ?!
                Impossible ! Vous vous rendez compte que vos traces laissées ont disparus ! Vous
                degainez votre arme, vous vous mettez aux aguets ! Tout d'un coup tout devient
                noir, vous sentez un coup de poignard dans le dos, puis dans le ventre, vous
                entendez des hurlements et des cris de plaisir.... des bandits... Vous mourrez
                lentements... Vous pensez à votre Famille... GAME OVER
                """
        else:
            a = \
                """
                Continuer tout droit vous donne des frissons, vous sentez avoir fait le
                bon choix. Vous continuez sur votre chemin, peu de temps après à la lisière de
                la fôret un bandit vous tend une embuscade ! 
                Arfff satané bandit. C'est l'heure du combat !

                Vous envoyez là ou ce bandit devrait etre ! En enfer !

                Vous sortez de la foret et voyez au loin votre chateau... Au pont levis vous voyez une
                troupes de cavalier se dirigez vers vous, vers votre fôret, vous reperez au loin
                l'armure reluisante de votre commandant, vous savez au fond de vous que cette
                petite brigade et venu à votre secours, vous vous sentez sauvé ! Vous decidez de
                prendre un temps de repos sur l'arbre le plus proche. Bien joué à vous !
                """
        print(a)
