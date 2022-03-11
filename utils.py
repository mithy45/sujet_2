# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:20:12 2022

@author: Quentin Brice Théo Micka Karim François
"""
def choose(display, choices):
    a = str()
    while a not in choices:
        a = input(f"{display} {choices} :\n\t").lower()
    return a
