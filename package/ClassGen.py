# -*- coding: utf-8 -*-

# Création d'une classe 'ClassGen' qui représente une classe générique
class ClassGen(object):

    # Le constructeur prend un argument 'name' et l'assigne à l'attribut d'instance 'name'
    def __init__(self, name):
        self.name = name

    # La méthode 'hello' affiche un message d'accueil qui comprend le 'name' de l'instance
    def hello(self):
        print(f"Hello i'm : {self.name}")