# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:28:28 2022

@author: gfmac
"""
from Mage import Mage
from Knight import Knight
from Warrior import Warrior



class Jeux:

    def __init__(self):
        self.name = "jeu de rôle"
        self.principale_player = None

    def main(self):
        name = input("Entrez votre nom :\n\t")
        job = input("Entrez votre classe (warrior, mage or knight) : \n\t")
        jobs = ["warrior", "mage", "knight"]
        while not (job in jobs):
            print("wrong jobs or syntax, try again")
            job = input("Entrez votre classe (warrior, mage or knight) : \n\t")
        if job == "mage":
            self.principale_player = Mage(name)
        elif job == "warrior":
            self.principale_player = Warrior(name)
        else:
            self.principale_player = Knight(name)
        self.principale_player.presentation()
        self.principale_player.speech()

