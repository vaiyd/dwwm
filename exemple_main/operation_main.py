# -*- coding: utf-8 -*-

# Fonction qui affiche 1, 2 ou 3 en fonction de la valeur de i (1 par défaut)
def if_exemple(i=1):
    
    # Si i est égal à 1, affiche 1
    if(i==1):
        print(1)
    # Si i est égal à 2, affiche 2
    elif(i==2):
        print(2)
    # Si i n'est ni 1 ni 2, affiche 3
    else:
        print(3)

    # Initialise bReturn à False
    bReturn = False
    # Si i est égal à 1, bReturn est défini à True
    if(i == 1):
        bReturn == True

# Fonction qui itère sur une liste donnée (ou [1, 2, 3, 4, 5, 6] par défaut) et affiche chaque élément
def for_exemple(arrayList = [1, 2, 3, 4, 5, 6]):

    # Pour chaque élément dans la liste, affiche l'élément
    for data in arrayList:
        print(data)

    # Affiche chaque nombre de 0 à 9
    for i in range(0,10):
        print(i)

# Fonction qui affiche les nombres de i (10 par défaut) à 0 dans l'ordre décroissant
def while_exemple(i = 10):
    
    # Tant que i n'est pas égal à 0, affiche i et décrémente i de 1
    while i != 0:
        print(i)
        i -= 1
    # Lorsque i est égal à 0, affiche 0
    else:
        print(0)

# Fonction qui essaie de diviser a par b (a est 1.0 par défaut et b est 0 par défaut) et gère l'erreur de division par zéro
def try_exemple(a=1.0, b=0):

    try :
        # Affiche "Start Division"
        print("Start Division")
        # Tente de diviser a par b et affiche le résultat
        print (a / b)

    # Si une erreur ZeroDivisionError est levée, affiche 'Error :: div par 0'
    except ZeroDivisionError :
        print ('Error :: div par 0')

    # Si aucune exception n'est levée, affiche "OK"
    else : 
        print("OK")

    # Qu'une exception soit levée ou non, affiche "End Division"
    finally : 
        print("End Division")

# Exécute les quatre fonctions définies ci-dessus
def main():
    if_exemple()
    for_exemple()
    while_exemple()
    try_exemple()

# Si ce fichier est le fichier principal exécuté, exécute la fonction main
if __name__ == '__main__':
    main()