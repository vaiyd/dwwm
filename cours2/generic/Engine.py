# -*- coding: utf-8 -*-

# Import de la classe User depuis le fichier User.py

# Import des outils nécessaires depuis le package SQLAlchemy
from sqlalchemy import create_engine, inspect as sql_inspect
from sqlalchemy.orm import Session

# Classe Engine pour la gestion de la base de données
class Engine(object):

    def __init__(self, type, user, mdp, sever, port, database):

        self.engine = create_engine(f"{type}://{user}:{mdp}@{sever}:{port}/{database}")
        self.session = Session(self.engine)

    # Fonction qui initialise la base de données
    def initializer(self, obj_class = None, as_table=True):

        obj = obj_class  # Instanciation de la classe passée en paramètre
        inspected = sql_inspect(self.engine) # Instanciation de l'inspecteur du SGBDR
        if obj:
            if not inspected.has_table(obj.__tablename__): # Si la table n'existe pas dans la base de données
                as_table = False
            if not as_table: # Si la table n'existe pas
                obj.__table__.create(self.engine)  # Création de la table dans la base de données

    def select_objects(self, obj):
        res = self.session.query(obj).all()  # Exécution de la requête et récupération des résultats
        return res  # Retour des résultats

    def selectObjectById(self, obj, obj_id):
        res = self.session.query(obj).filter_by(id=obj_id).first() # Exécution de la requête et récup un resultat unique
        return res  # Retour de l'objet récupéré

    # Fonction qui insère un nouvel utilisateur dans la base de données
    def addObject(self, obj):
        b_return = False  # Valeur par défaut de la variable de retour
        try:
            b_return = True
            self.session.add(obj)  # Ajout du nouvel utilisateur à la session
            self.session.commit()  # Validation des changements dans la base de données
        except Exception as e:
            print(f"Error during insertion :: {e}")  # Gestion des erreurs lors de l'insertion
        return b_return  # Retour du succès ou de l'échec de l'opération
