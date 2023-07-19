# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from .resources import GarageResource

# Initialisation de l'application Flask
app = Flask("DWWM")
# Initialisation de l'API Flask-RESTful
api = Api(app)

# Ajout de la ressource Voiture à l'API avec l'endpoint /voiture
api.add_resource(GarageResource.VoitureResource, '/voiture')