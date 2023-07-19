# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api

from .resources import GarageResource

app = Flask("DWWM")
api = Api(app)

api.add_resource(GarageResource.VoitureResource, '/voiture')