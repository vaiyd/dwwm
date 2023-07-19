# -*- coding: utf-8 -*-
"""

@author: Baptiste
"""
from flask_restful import Resource
from flask import request

class GenericResource(Resource):

    def __init__(self, serviceController = None):
        '''
        Constructor
        '''

        self.serviceController = serviceController

    def rebuild_params(self):
        # On vérifie si les données ont été envoyées sous forme de formulaire ou de JSON, et on les stocke dans un dictionnaire
        new_dict = {}
        if(request.form != {}):
            args = request.form
            new_dict = args.to_dict()
        if(request.json != {}):
            new_dict = request.json

        return new_dict
    