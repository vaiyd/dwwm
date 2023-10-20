# -*- coding: utf-8 -*-
'''

Exercice 3 : Gestionnaire de tâches avec une base de données et une API permettant l'accès

1. Installez Flask et Flask-RESTful si vous ne l'avez pas déjà fait.

2. Créez un nouveau fichier pour votre application Flask.

3. Configurez une API avec Flask-RESTful et créez des routes qui correspondent aux opérations CRUD que nous
avons définies précédemment (par exemple, GET pour récupérer les tâches, POST pour créer une nouvelle tâche,
PUT pour mettre à jour une tâche, et DELETE pour supprimer une tâche).

4. Chaque route doit interagir avec la base de données, effectuant l'opération
correspondante en fonction de la requête reçue.

5. Verifier votre API en utilisant un outil comme curl ou Postman ou requests pour 
envoyer des requêtes à votre application et observer les réponses.

'''

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from exercices.exercice2.task_db import get_all_tasks, get_task_from_id, create_task, update_task, delete_task

from flask import Flask, request, jsonify
from flask_restful import Api
from cours2.generic.GenericResource import GenericResource

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

class TaskResource(GenericResource):
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

api.add_resource(TaskResource, '/task')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)