# -*- coding: utf-8 -*-

from .Vehicule import Vehicule  # Importation de la classe 'ClassGen'
from .Roue import Roue  # Importation de la classe 'Class2'

# Création d'une classe 'Class1' qui hérite de 'ClassGen'
class Voiture(Vehicule):

    # Le constructeur prend un argument 'name' et un argument facultatif 'class2'
    def __init__(self, marque):
        self.roues = [Roue(position="AVG"), Roue(position="AVD"), Roue(position="ARG"), Roue(position="ARD")]
        
        Vehicule.__init__(self, marque)
    
    def info(self):

        for roue in self.roues :
            print(roue.position)

        Vehicule.info(self)
        

