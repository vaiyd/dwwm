# -*- coding: utf-8 -*-

from package.Voiture import Voiture
from orm.controller.GarageController import GarageController

def main():

    voiture1 = Voiture("BMW")
    voiture1.info()

def sql_main():

    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import Session

    engine = create_engine("mysql://root:wordpress@uat-bdn.bmcorp.fr:3306/dwwm_orm")
    
    session = Session(engine)

    req = text("""SELECT * FROM marque_lookup""")
    
    res = session.execute(req).all()

    print(res)

def buildTables():
    grCtrl = GarageController()
    grCtrl.initGarage()

def orm_main():

    grCtrl = GarageController()
    pass

if __name__ == '__main__':

    main()
    #sql_main()
    #orm_main()