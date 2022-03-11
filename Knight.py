# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 10:13:02 2022

@author: gfmac
"""
from Character import Character

class Knight(Character):
    def __init__(self, name, ad=30, max_hp=120):
        super().__init__(name, "Knight", max_hp, ad, max_hp)