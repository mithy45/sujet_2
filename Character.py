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
        print(f"Je suis {self.name} héritié de Jeanne d'arc, et je suis un {self.job}")