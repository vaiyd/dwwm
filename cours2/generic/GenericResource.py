# -*- coding: utf-8 -*-

"""
@author: Baptiste
"""
from flask_restful import Resource
from flask import request

# Classe générique pour les ressources API
class GenericResource(Resource):

    def __init__(self, serviceController = None):
        '''
        Constructeur
        '''
        # Initialisation avec un contrôleur de service par défaut à None
        self.serviceController = serviceController

    # Méthode pour reconstruire les paramètres d'une requête
    def rebuild_params(self):
        # Vérification si les données ont été envoyées sous forme de formulaire ou de JSON
        # et stockage de ces données dans un dictionnaire
        new_dict = {}
        if(request.form != {}):
            args = request.form
            new_dict = args.to_dict()
        elif(request.json != {}):
            new_dict = request.json

        return new_dict