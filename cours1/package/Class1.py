# -*- coding: utf-8 -*-

from .ClassGen import ClassGen  # Importation de la classe 'ClassGen'
from .Class2 import Class2  # Importation de la classe 'Class2'

# Création d'une classe 'Class1' qui hérite de 'ClassGen'
class Class1(ClassGen):

    # Le constructeur prend un argument 'name' et un argument facultatif 'class2'
    def __init__(self, name, class2=None):
        self.typ="class1"
        self.child = class2 or Class2()  # Initialise l'attribut 'child' à 'class2' ou à une nouvelle instance de 'Class2' si 'class2' n'est pas fourni
        
        ClassGen.__init__(self, name)