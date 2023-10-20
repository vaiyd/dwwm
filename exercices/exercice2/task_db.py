# -*- coding: utf-8 -*-
'''
Exercice 2 : Gestionnaire de tâches avec une base de données
 
1. Installez SQLAlchemy si vous ne l'avez pas déjà fait.
2. Créez un fichier SQLite tasks.db.
3. Définissez une classe Task avec SQLAlchemy qui représente les éléments de votre liste de tâches. Chaque tâche doit avoir les attributs suivants :
    ID (clé primaire)
    Title (titre de la tâche)
    Description (description de la tâche)
    Completed (indique si la tâche a été complétée ou non, booléen)
4. Écrivez des procdéures ou fonctions pour effectuer les opérations CRUD suivantes :
    Créer une nouvelle tâche
    Récupérer toutes les tâches
    Mettre à jour le statut d'une tâche (complétée ou non complétée)
    Supprimer une tâche
'''

from sqlalchemy import text, create_engine, Column, Integer, String, Text, Boolean
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    title = Column(String(63), unique=True)
    description = Column(Text)
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return (f"id :: {self.id} ; title :: {self.title} ; description :: {self.description} ; completed :: {self.completed}")

    def to_dict(self):
        return ({"id":self.id, "title":self.title,
                 "description":self.description, "completed":self.completed})

def session_commit(session):
    try:
        session.commit()
    except Exception as e:
        print(f"Une erreur est surevenue :: {e}")
        session.rollback()

def get_task_from_id(session, id):
    task = session.query(Task).filter_by(**{"id":id}).first()
    return task

def get_all_tasks(session):
    tasks = session.query(Task).all()
    return tasks

def create_task(session, **kwargs):
    new_task = Task(**kwargs)
    session.add(new_task)
    session_commit(session=session)

def update_task(session, id, title=None,description=None, completed=None):
    task = get_task_from_id(session=session, id=id)
    if(task != None):
        if(title != None):
            task.title = title
        if(completed != None):
            task.completed = completed
        if(description != None):
            task.description = description
        session_commit(session=session)
        return task
    else:
        return False

def delete_task(session, id):
    task = get_task_from_id(session=session, id=id)
    if(task != None):
        session.delete(task)
        session_commit(session=session)
        return id
    else:
        return False

def main():

    engine = create_engine('sqlite:///tasks.db')
    Base.metadata.create_all(engine)

    session = Session(engine)
    
    req = text("""SELECT * FROM task""")
    res = session.execute(req).all()
    print(res)

    #create_task(session=session, title="titre2", description="dc2")

    '''tasks = get_all_tasks(session=session)
    for task in tasks:
        print(task)'''

    #print(get_task_from_id(session=session, id=3))

    #update_task(session=session, id=1, completed=True)

    #delete_task(session=session, id=1)

    #create_task(session=session, title="titre4", description="dc4")

if __name__ == '__main__':
    main()

