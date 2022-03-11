# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:28:28 2022

@author: gfmac
"""

from random import randint
import Character

class Jeux:
    
    def __init__(self):
        self.name = "jeu de rôle"
        
    def main(self):
        print("enter name : ")
        name = input()
        job = input("enter job (warrior, mage or knight) : \n")
        jobs = ["warrior", "mage", "knight"]
        while (not(job in jobs)):
            print("wrong jobs or syntax, try again")
            job = input("enter job (warrior, mage or knight) : \n")
        max_hp = randint(5, 20)
        ad = randint(5, 20)
        character = Character(name, job, max_hp, ad, max_hp) 