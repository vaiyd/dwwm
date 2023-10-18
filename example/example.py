# -*- coding: utf-8 -*-

import json

class class1:

    def __init__(self, nom="nom1", description="description1"):
        self.nom = nom
        self.description = description


def main():

    c = class1()
    #print(c.nom)
    c_dict = c.__dict__
    #print(c_dict)
    #print(json.dumps(c_dict))

    '''for key, value in i.items() :
        for val in value:
            pass
            #print(val)'''


    '''dict_data = {"mess1":"hello", "mess2":"epsi"}
    print(dict_data)
    del dict_data["mess2"]
    print(dict_data)'''




    '''i=0
    run = True
    while run:
        i = 1 + 1
        
        if(i == 10):
            run = False'''


if __name__ == '__main__':
    main()