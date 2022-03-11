# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:20:12 2022

@author: Quentin Brice Théo Micka Karim François
"""
from utils import choose


class Combat:
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2

    def fight(self):
        while self.character1.is_alive() and self.character2.is_alive():
            if not self.character1.monster:
                choice = choose("Que voulez-vous faire comme action ? ", ["fuir", "combattre"])
                if choice == "fuir":
                    print("Vous fuyez...")
                    return
                else:
                    self.character1.attack(self.character2)
            else:
                self.character1.attack(self.character2)
            if self.character2.is_alive():
                if not self.character2.monster:
                    choice = choose("Que voulez-vous faire comme action ? ", ["fuir", "combattre"])
                    if choice == "fuir":
                        print("Vous fuyez...")
                        return
                    else:
                        self.character2.attack(self.character1)
                else:
                    self.character2.attack(self.character1)
        if not self.character1.is_alive():
            print(f"{self.character1.name} est mort au combat !")
        else:
            print(f"{self.character2.name} est mort au combat !")

