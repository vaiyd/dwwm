# -*- coding: utf-8 -*-

# Création d'une classe 'Vehicule' qui représente une classe générique
class Vehicule(object):

    # Le constructeur prend un argument 'name' et l'assigne à l'attribut d'instance 'name'
    
    def __init__(self, marque):
        self.marque = marque

    # La méthode 'hello' affiche un message d'accueil qui comprend le 'name' de l'instance
    def info(self):
        print(f"Hello i'm : {self.marque}")