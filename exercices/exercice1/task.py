# -*- coding: utf-8 -*-

'''

Exercice : Gestionnaire de tâches
 
Description : Créez un programme simple de "gestionnaire de tâches" qui permet à un utilisateur d'ajouter des tâches,
de les voir et de les supprimer. Chaque tâche a deux attributs : le nom et la description.
 
Fonctionnalités :
1.	Ajouter une tâche (nom, description).
2.	Afficher toutes les tâches.
3.	Supprimer une tâche spécifique.
4.	Quitter le programme
 
Consignes :
•	Utilisez des fonctions.
•	Implémentez une boucle pour continuer à exécuter le programme jusqu'à ce que l'utilisateur décide de quitter.
•	Manipulez les erreurs potentielles comme l'ajout d'une tâche sans nom ou la suppression d'une tâche qui n'existe
    pas.
'''

def add_task(tasks, name, description):
    tasks[name] = description
    print(f"Tâche ajouté : {name}")

def show_tasks(tasks):
    if not tasks :
        print ("Aucune tâche à afficher")
    else:
        for name, description in tasks.items():
            print(f"Nom : {name}, description : {description}")

def remove_task(tasks, name):
    if name in tasks:
        del tasks[name]
        print(f"Tâche {name} supprimée avec succès")
    else:
        print(f"La tâche {name} n'existe pas")

def main():
    tasks = {}

    start = True
    while start:
        print("\nGestionnaire des tâches")
        print("1. Ajouter une tâche")
        print("2. Voir toutes les tâches")
        print("3. Supprimer une tâche")
        print("4. Quitter le programme")

        choice = input("Choix de commande : ")

        if(choice == "1"):
            name = input("Entrez le nom de la tâche : ").strip()
            description = input("Entrez la description : ").strip()

            if(name):
                add_task(tasks=tasks, name=name, description=description)
            else:
                print("Le nom est requis pour la créer une tâche")

        elif(choice == "2"):
            show_tasks(tasks=tasks)

        elif(choice == "3"):
            name = input("Entrez le nom de la tâche à supprimer : ").strip()
            remove_task(tasks=tasks, name=name)

        elif(choice == "4"):
            start =False
            print("Au revoir")
        
        else:
            print("Choix invalide")

if __name__ == '__main__':
    main()
