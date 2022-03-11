# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:20:12 2022

@author: gfmac
"""
from abc import abstractmethod


class Character:

    def __init__(self, name, job, current_hp, ad, max_hp):
        self.name = name
        self.job = job
        self.current_hp = current_hp
        self.ad = ad
        self.max_hp = max_hp

    def attack(self, ennemy):
        ennemy.get_damage(self.ad)

    @abstractmethod
    def get_damage(self, ad):
        pass

    @abstractmethod
    def speech(self):
        pass

    def presentation(self):
        a = \
        f"""
        Bonjour {self.name}, du haut de vos 25ans, vous etes le meilleure {self.job} du Royaume de Kaslow, malheuresment vous
        vous êtes fait teleporter dans la foret de Fark, là ou les monstres les plus
        terrifiants rode ! 
        Vous vous remettez à peinde de vos esprits que vous vous faites deja agresser par
        un Kobolt ! Vous vous saisissez de votre arme et engagez le combat ! 
        """
        print(a)