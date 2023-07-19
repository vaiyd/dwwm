# -*- coding: utf-8 -*-
"""

@author: Baptiste
"""

from cours2.generic.GenericResource import GenericResource
from cours2.orm.controller.GarageController import GarageController

class VoitureResource(GenericResource):

    def __init__(self):
        '''
        Constructor
        '''
        GenericResource.__init__(self, serviceController = GarageController())
        self.serviceController.init()
    
    def get(self):
        res  = []
        voitures = self.serviceController.selectVoitures()
        if voitures is None or voitures == []:
            return {'message': 'Voiture not found'}, 404
        else:
            for v in voitures:
                res.append(v.to_dict())
        return res, 200  # vars() convertit l'objet Voiture en dict
    
    def post(self):
        data = self.rebuild_params()
        res = self.serviceController.insertVoiture(data)
        if(res == False):
            return {'message': 'Voiture not found'}, 404
        else:
            return res, 201