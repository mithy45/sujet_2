# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:20:12 2022

@author: Quentin Brice Théo Micka Karim François
"""
from Mage import Mage
from Knight import Knight
from Warrior import Warrior
from utils import choose


class Jeux:

    def __init__(self):
        self.name = "jeu de rôle"
        self.principale_player = None

    def main(self):
        name = input("Entrez votre nom :\n\t")
        jobs = ["guerrier", "mage", "chevalier"]
        job = choose("Entrez votre classe ", jobs)
        if job == "mage":
            self.principale_player = Mage(name)
        elif job == "guerrier":
            self.principale_player = Warrior(name)
        else:
            self.principale_player = Knight(name)
        self.principale_player.presentation()
        self.principale_player.speech()

