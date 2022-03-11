# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:28:28 2022

@author: gfmac
"""

from random import randint
from Character import Character
from Mage import Mage
from Knight import Knight
from Warrior import Warrior


class Jeux:

    def __init__(self):
        self.name = "jeu de rôle"
        self.principale_player = None

    def main(self):
        name = input("enter name : \n")
        job = input("enter job (warrior, mage or knight) : \n")
        jobs = ["warrior", "mage", "knight"]
        while not (job in jobs):
            print("wrong jobs or syntax, try again")
            job = input("enter job (warrior, mage or knight) : \n")
        if job == "mage":
            self.principale_player = Mage()
        elif job == "warrior":
            self.principale_player = Warrior()
        else:
            self.principale_player = Knight()

        self.principale_player.presentation()
        self.principale_player.speech()

