# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from cours1.package.Voiture import Voiture
from cours2.orm.controller.GarageController import GarageController

def main():

    voiture1 = Voiture("BMW")
    voiture1.info()

def sql_main():

    engine = create_engine("mysql://<user>:<pass>@192.168.10.174:3306/dwwm")
    session = Session(engine)

    req = text("""SELECT * FROM marque_lookup""")
    res = session.execute(req).all()
    #test sonar
    print(res)

def buildTables():
    grCtrl = GarageController()
    grCtrl.init()

def orm_main():

    grCtrl = GarageController()
    pass

if __name__ == '__main__':

    #main()
    sql_main()
    #buildTables()
