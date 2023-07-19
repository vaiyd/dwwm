# -*- coding: utf-8 -*-

def initUse():
    # Affiche "Hello World"
    print("Hello World")

    # Effectue une addition, l'affiche et affiche une phrase contenant le résultat
    print("---------------------")
    a = 1 + 1
    print(a)
    print(f"Resultats : {a}")

    # Montre différentes façons d'accéder à des sous-chaînes
    print("---------------------")
    s = "monexemple.py"

    print(s[3])  # Affiche le 4e caractère
    print(s[-5])  # Affiche le 5e caractère en partant de la fin
    print(s[2:5])  # Affiche les 3e à 5e caractères
    
    print(s[:5])  # Affiche les 5 premiers caractères
    print(s[0:5])  # C'est la même chose que s[:5]
    
    print(s[3:])  # Affiche la chaîne à partir du 4e caractère
    print(s[3:len(s)])  # C'est la même chose que s[3:]

def listUse():
    # Montre différentes opérations sur une liste
    print("---------------------")
    a = ['spam', 'eggs', 100, 1234] 

    # Ajoute un nouvel élément à la liste
    a.append("new")
    print(a.index("new"))  # Affiche l'index du nouvel élément
    print(a)

    print(f"append :: {a[4]}")
    print(len(a))  # Affiche la longueur de la liste

    a.remove("new")  # Supprime l'élément "new" de la liste

    a.reverse()  # Inverse l'ordre des éléments de la liste
    print(a)

    # Affiche une liste complexe
    s = ['abc', [(1,2), ([3], 4)], 5]
    print(s)

def dictUse():
    # Montre différentes opérations sur un dictionnaire
    print("---------------------")

    dico = {"japon":"tokyo","france":"paris"}
    print(f"create :: {dico}")
    print(type(dico))  # Affiche le type de l'objet dico
    
    dico["japon"] = "kyoto"  # Modifie la valeur associée à "japon"
    print(f"append :: {dico}")

    del dico["france"]  # Supprime la paire "france":"paris"
    print(f"del :: {dico}")

    # Ajoute deux nouvelles paires au dictionnaire
    dico["france"] = "paris"
    dico["suisse"] = "berne"

    print(dico)

    # Trouve toutes les clés qui ont "paris" comme valeur
    fr = [k for k, v in dico.items() if v == 'paris']
    print(fr)

    # Différentes façons d'accéder aux valeurs d'un dictionnaire
    print(dico["japon"])
    print(dico.get("japon"))

    # Montre comment gérer une clé qui n'est pas dans le dictionnaire
    br = dico.get("bresil")
    print(br)
    print(type(br))
    if(br != None):
        print("OK")
    dico1 = {1:"test1","2":"test2"}  # Montre un dictionnaire avec des clés de types différents
    print(dico1)  # Affiche le dictionnaire

def request():
    import requests
    import json

    response = requests.get("https://google.fr")  # Fait une requête GET à google.fr

    # Fait une requête GET à l'API de OpenLibrary et convertit la réponse en JSON
    responseBook = requests.get("https://openlibrary.org/isbn/9780747542988.json")
    res = responseBook.json()

    print(type(res))  # Affiche le type de l'objet res
    print(res)  # Affiche le contenu de res

    # Parcourt toutes les paires clé-valeur dans res et les affiche
    for key, value in res.items() :
        print (f"{key} :: {value}")
    
    print(res.get("identifiers"))  # Affiche la valeur associée à "identifiers" dans res

def main():
    #initUse()
    #listUse()
    #dictUse()
    request()  # Exécute la fonction request()

# Si ce fichier est le fichier principal exécuté, exécute la fonction main()
if __name__ == '__main__':
    main()