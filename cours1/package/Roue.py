# -*- coding: utf-8 -*-

# Création d'une classe 'Class2' qui hérite de 'ClassGen'
class Roue(object):

    # Le constructeur prend un argument 'name' avec une valeur par défaut, et initialise 'typ' à 'class2'
    def __init__(self, position, diametre = 18):
        self.position = position
        self.diametre=diametre

