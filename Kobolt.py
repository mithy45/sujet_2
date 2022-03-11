# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:20:12 2022

@author: Quentin Brice Théo Micka Karim François
"""
from Character import Character


class Kobolt(Character):
    def __init__(self, name="Vilain", ad=15, max_hp=50, res=0.75, monster=True, ia=True):
        super().__init__(name, "Kobolt", max_hp, ad, max_hp, res, monster, ia)

    def speech(self):
        pass
