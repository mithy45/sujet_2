# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:20:12 2022

@author: gfmac
"""
from abc import abstractmethod


class Character:

    def __init__(self, name, job, current_hp, ad, max_hp, res, monster):
        self.name = name
        self.job = job
        self.current_hp = current_hp
        self.ad = ad
        self.max_hp = max_hp
        self.res = res
        self.monster = monster

    def attack(self, ennemy):
        print(f"{self.name} : Prend ça !")
        ennemy.get_damage(self.ad)

    def get_damage(self, ad):
        dmg = int(ad * self.res)
        self.current_hp -= dmg
        if self.current_hp < 0:
            self.current_hp = 0
        print(f"{self.name} : Ouch.. -{dmg}hp.. Il reste {self.current_hp}hp à {self.name}")

    def restore_hp(self, hp):
        print(f"\tCa fait du bien.. + {hp}hp")
        self.current_hp += hp
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def is_alive(self):
        return self.current_hp > 0

    @abstractmethod
    def speech(self):
        pass

    def presentation(self):
        a = \
            f"""
        Bonjour {self.name}, du haut de vos 25ans, vous êtes le meilleur {self.job} du Royaume de Kaslow.
        """
        print(a)
