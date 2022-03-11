# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 10:13:02 2022

@author: gfmac
"""
from Character import Character


class Knight(Character):
    def __init__(self, name, ad=30, max_hp=120):
        super().__init__(name, "Knight", max_hp, ad, max_hp)

    def __init__(self):
        super().__init__("Quentin", "Knight", 120, 30, 120)

    def get_damage(self, ad):
        self.current_hp -= int(ad * 0.50)
        if self.current_hp < 0:
            self.current_hp = 0
