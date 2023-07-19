# -*- coding: utf-8 -*-

from package.Class1 import Class1  # Importation de la classe 'Class1'
from package.Class2 import Class2  # Importation de la classe 'Class2'
    

def main():

    # Création d'une instance de 'Class1' nommée 'num1' avec 'name' défini comme 'PARENT1' et 'class2' défini comme une nouvelle instance de 'Class2' avec 'name' défini comme 'New_Child1'
    num1 = Class1(name="PARENT1", class2=Class2(name="New_Child1"))
    
    num1.hello()  # Appel de la méthode 'hello' sur 'num1'
    print(num1.typ)  # Affiche le type de 'num1'

    num1.child.hello()  # Appel de la méthode 'hello' sur l'attribut 'child' de 'num1'
    print(num1.child.typ)  # Affiche le type de l'attribut 'child' de 'num1'
    
if __name__ == '__main__':
    main()  # Exécute la fonction main si ce fichier est le fichier principal exécuté
