# -*- coding: utf-8 -*-

"""
@author: Baptiste
"""

from cours2.generic.GenericResource import GenericResource
from cours2.orm.controller.GarageController import GarageController

# Classe pour la ressource Voiture, dérivée de la ressource générique
class VoitureResource(GenericResource):

    def __init__(self):
        '''
        Constructeur
        '''
        # Initialisation de la ressource générique avec le contrôleur de garage
        GenericResource.__init__(self, serviceController = GarageController())
        # Initialisation du contrôleur de service
        self.serviceController.init()

    # Méthode GET pour récupérer les voitures
    def get(self):
        res  = []
        voitures = self.serviceController.selectVoitures()
        # Si aucune voiture n'est trouvée, renvoie un message d'erreur
        if voitures is None or voitures == []:
            return {'message': 'Voiture not found'}, 404
        else:
            # Sinon, transforme chaque voiture en dictionnaire et l'ajoute à la liste des résultats
            for v in voitures:
                res.append(v.to_dict())
        return res, 200

    # Méthode POST pour ajouter une nouvelle voiture
    def post(self):
        # Reconstruction des paramètres de la requête
        data = self.rebuild_params()
        # Insertion de la nouvelle voiture
        res = self.serviceController.insertVoiture(data)
        # Si l'insertion a échoué, renvoie un message d'erreur
        if(res == False):
            return {'message': 'Voiture not found'}, 404
        else:
            # Sinon, renvoie la nouvelle voiture et un code de succès
            return res, 201
