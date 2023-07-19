# -*- coding: utf-8 -*-

# Importation des classes de modèles et de l'Engine ORM
from ..model.Garage import MarqueLookup, Voiture, Roue, VoitureRoue
from ...generic.Engine import Engine

# Classe GarageController pour gérer les interactions entre l'ORM et les APIs
class GarageController(object):

    # Initialisation du contrôleur
    def __init__(self):

        # Création d'une instance de l'Engine ORM avec les informations de connexion à la base de données
        self.orm = Engine(type='mysql', user='root', mdp='wordpress', sever='192.168.10.174', port='3306', database='dwwm')

    # Méthode pour sélectionner toutes les voitures dans la base de données
    def selectVoitures(self):
        res = []
        # Utilisation de l'Engine ORM pour sélectionner tous les objets Voiture
        res = self.orm.selectObjects(Voiture)
        # Retourne les résultats de la sélection
        return res

    # Méthode pour sélectionner tous les objets VoitureRoue dans la base de données
    def selectVoituresRoues(self):
        res = []
        # Utilisation de l'Engine ORM pour sélectionner tous les objets VoitureRoue
        res = self.orm.selectObjects(VoitureRoue)
        # Retourne les résultats de la sélection
        return res

    # Méthode pour sélectionner toutes les marques dans la base de données
    def selectMarques(self):
        res = []
        # Utilisation de l'Engine ORM pour sélectionner tous les objets MarqueLookup
        res = self.orm.selectObjects(MarqueLookup)
        # Retourne les résultats de la sélection
        return res

    # Méthode pour insérer une nouvelle voiture dans la base de données
    def insertVoiture(self, data):
        # Création d'une nouvelle instance de Voiture à partir des données fournies
        v = Voiture(**data)
        # Utilisation de l'Engine ORM pour ajouter la nouvelle voiture à la base de données
        res = self.orm.addObject(v)
        # Si l'ajout a réussi, convertit la nouvelle voiture en dictionnaire, sinon retourne False
        if(res):
            v = v.to_dict()
        else:
            v = False
        return v

    # Méthode pour créer une nouvelle voiture Polo
    def createPolo(self):
        # Création d'une nouvelle instance de Voiture avec le modèle Polo et la marque Volkswagen
        polo = Voiture(modele="POLO")
        polo.marque = MarqueLookup(label = "VOLKSWAGEN")
        # Ajout de la nouvelle voiture à la base de données
        self.orm.addObject(polo)
        # Affichage du label de la marque de la nouvelle voiture
        print(polo.marque.label)

    # Méthode pour initialiser les tables de la base de données pour les objets MarqueLookup, Roue, Voiture, VoitureRoue
    def init(self):
        self.orm.initializer(MarqueLookup)
        self.orm.initializer(Roue)
        self.orm.initializer(Voiture)
        self.orm.initializer(VoitureRoue)
