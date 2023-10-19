# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from exercices.exercice2.task_db import get_all_tasks, get_task_from_id, create_task, update_task, delete_task

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

Base = declarative_base()

engine = create_engine('sqlite:///tasks.db')
Base.metadata.create_all(engine)

session = Session(engine)

app = Flask("poec")
api = Api(app)

'''
GET = selection/lecture
POST = envoi de formulaire -> insertion
PUT = envoi de formulaire -> mise à jour
DELETE = envoi de formulaire -> suppression

'''
class GenericResource(Resource):
    # Méthode pour reconstruire les paramètres d'une requête
    def rebuild_params(self):
        # Vérification si les données ont été envoyées sous forme de formulaire ou de JSON
        # et stockage de ces données dans un dictionnaire
        new_dict = {}
        if(request.form != {}):
            args = request.form
            new_dict = args.to_dict()     
        if(request.json != {}):
            new_dict = request.json

        return new_dict

class Example(GenericResource):
    def get(self):
        
        final_tasks = []
        tasks = get_all_tasks(session=session)

        for task in tasks:
            final_tasks.append(task.to_dict())

        return final_tasks
    
    def post(self):
        data = self.rebuild_params()
        return jsonify(data)
    
    def put(self):
        pass

    def delete(self):
        pass

api.add_resource(Example, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)