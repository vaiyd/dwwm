# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()

class ExampleTable(Base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    data = Column(String)

    def __repr__(self):
        return (f"{self.id} :: {self.data}")

    def to_dict(self):
        return ({"id":self.id, "data":self.data})

def main():

    engine = create_engine('sqlite:///test.db')
    Base.metadata.create_all(engine)

    session = Session(engine)
    list_example = session.query(ExampleTable).all()
    
    for example in list_example:
        print(example.to_dict())
        #print(f"{example.id} :: {example.data}")

    #test1 = session.query(ExampleTable).filter(ExampleTable.id == 1).first()
    #test1 = session.query(ExampleTable).filter_by(**{"id":1}).first()
    
    '''test = ExampleTable(data="text_test2")
    session.add(test)
    session.commit()'''
    

if __name__ == '__main__':
    main()

