# -*- coding: utf-8 -*-

from ..model.Garage import MarqueLookup, Voiture, Roue, VoitureRoue
from ..generic.Engine import Engine

# Classe GarageController pour l'achange entre l'ORM et les APIs
class GarageController(object):

    def __init__(self):

        self.orm = Engine(user='root', mdp='wordpress', sever='uat-bdn.bmcorp.fr', port='3306', database='dwwm_orm')

    def initGarage(self):
        
        self.orm.initializer(MarqueLookup)
        self.orm.initializer(Roue)
        self.orm.initializer(Voiture)
        self.orm.initializer(VoitureRoue)