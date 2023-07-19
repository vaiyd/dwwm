# -*- coding: utf-8 -*-

from .ClassGen import ClassGen  # Importation de la classe 'ClassGen'

# Création d'une classe 'Class2' qui hérite de 'ClassGen'
class Class2(ClassGen):

    # Le constructeur prend un argument 'name' avec une valeur par défaut, et initialise 'typ' à 'class2'
    def __init__(self, name="CHILD1"):
        self.typ="class2"
        ClassGen.__init__(self, name)  # Appelle le constructeur de la classe parente 'ClassGen'
