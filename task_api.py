# -*- coding: utf-8 -*-
'''

Exercice 3 : Gestionnaire de tâches avec une base de données et une API permettant l'accès

1. Installez Flask et Flask-RESTful si vous ne l'avez pas déjà fait.

2. Créez un nouveau fichier pour votre application Flask.

3. Configurez une API avec Flask-RESTful et créez des routes qui correspondent aux opérations CRUD que nous
avons définies précédemment (par exemple, GET pour récupérer toutes les tâches, POST pour créer une nouvelle tâche,
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

class TaskListResource(GenericResource):
    def get(self):
        final_tasks = []
        final_tasks = self.rebuild_tasks(final_tasks=final_tasks)

        return final_tasks
    
    def post(self):
        final_tasks = []
        data = self.rebuild_params()
        create_task(session=session, **data)
        final_tasks = self.rebuild_tasks(final_tasks=final_tasks)

        return final_tasks

    def rebuild_tasks(self, final_tasks):
        tasks = get_all_tasks(session=session)

        for task in tasks:
            final_tasks.append(task.to_dict())

        return final_tasks

class TaskResource(GenericResource):
    def get(self, task_id):
        task = get_task_from_id(session=session, id=task_id)
        if(task == None):
            return {"message":"Tâche non trouvée"}, 400
        return task.to_dict()
    
    def put(self, task_id):
        data = self.rebuild_params()
        task = update_task(session=session, id=task_id, **data)
        if(not task):
            return {"message":"Tâche non trouvée"}, 400
        return task.to_dict()

    def delete(self, task_id):
        delete_id = delete_task(session=session, id=task_id)
        if(not delete_id):
            return {"message":"Problème de suppression"}, 400
        return {"message":f"Tâche {delete_id} supprimée"}

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)