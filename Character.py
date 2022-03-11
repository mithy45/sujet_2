# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:20:12 2022

@author: gfmac
"""


class Character:

    def __init__(self, name, job, current_hp, ad, max_hp):
        self.name = name
        self.job = job
        self.current_hp = current_hp
        self.ad = ad
        self.max_hp = max_hp

    def attack(self, ennemy):
        ennemy.current_hp -= self.ad
