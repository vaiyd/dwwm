# -*- coding: utf-8 -*-
#pylint: disable=line-too-long
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
#pylint: enable=line-too-long

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from flask import Flask
from flask_restful import Api
from cours2.generic.GenericResource import GenericResource
from exercices.exercice2.task_db import create_task, get_all_tasks, get_task_from_id, update_task, delete_task

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
    """
    Permet d'afficher une liste de tâches et d'en créer
    """
    def get(self):
        """
        Permet d'afficher une liste de tâches
        Args:
            self : la classe TaskListResource
        Return:
            final_tasks : list : toutes les tâches
        """
        final_tasks = []
        final_tasks = self.rebuild_tasks(final_tasks=final_tasks)
        return final_tasks

    def post(self):
        """
        Permet de créer des tâches
        Args:
            self : la classe TaskListResource
        Return:
            list : toutes les tâches
        """
        final_tasks = []
        data = self.rebuild_params()
        create_task(session=session, **data)
        final_tasks = self.rebuild_tasks(final_tasks=final_tasks)

        return final_tasks

    def rebuild_tasks(self, final_tasks):
        """
        Recontruit les objets tâche en list de dictionnaire
        Args:
            self : la classe TaskListResource
            final_tasks : list : liste de tâches
        Return:
            final_tasks : list : toutes les tâches au format dict
        """
        tasks = get_all_tasks(session=session)

        for task in tasks:
            final_tasks.append(task.to_dict())

        return final_tasks

class TaskResource(GenericResource):
    """
    Gestion des opérations API qui concernent une tâche spécifique.

    Cette classe gère les requêtes HTTP destinées aux tâches individuelles, permettant 
    de récupérer, mettre à jour, ou supprimer des tâches spécifiques par leur identifiant.

    Méthodes
    --------
    get(task_id: int):
        Récupère une tâche par son identifiant unique.
    put(task_id: int):
        Met à jour une tâche spécifique par son identifiant, avec les nouvelles données fournies.
    delete(task_id: int):
        Supprime une tâche spécifique de la base de données par son identifiant.
    """
    
    def get(self, task_id):
        """
        Récupère une tâche par son id
        Args:
            self : la classe TaskResource
            task_id : int : l'id de la tâche
        Return:
            task : dict : une tâche formatté en dictionnaire
        """
        task = get_task_from_id(session=session, id=task_id)
        if task is None:
            return {"message":"Tâche non trouvée"}, 400
        return task.to_dict()

    def put(self, task_id):
        """
        Mets à jour une tâche par son id
        Args:
            self : la classe TaskResource
            task_id : int : l'id de la tâche
        Return:
            dict : message d'erreur
            task : dict : une tâche
        """
        data = self.rebuild_params()
        task = update_task(session=session, id=task_id, **data)
        if not task:
            return {"message":"Tâche non trouvée"}, 400
        return task.to_dict()

    def delete(self, task_id):
        """
        Supprimer une tâche par son id
        Args:
            self : la classe TaskResource
            task_id : int : l'id de la tâche
        Return:
            dict : message d'erreur
            dict : message de réussite
        """
        delete_id = delete_task(session=session, id=task_id)
        if not delete_id:
            return {"message":"Problème de suppression"}, 400
        return {"message":f"Tâche {delete_id} supprimée"}

api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)
