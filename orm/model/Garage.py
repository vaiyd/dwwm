from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MarqueLookup(Base):
    __tablename__ = 'marque_lookup'
    id = Column(Integer, primary_key=True, autoincrement=True)
    label = Column(String(50), nullable=False)

class Roue(Base):
    __tablename__ = 'roue'
    id = Column(Integer, primary_key=True, autoincrement=True)
    marque = Column(String(100))
    diametre = Column(Integer)
    type = Column(String(100))
    position = Column(String(50), nullable=False)

    voitures = relationship("Voiture", secondary='voiture_roue')

class Vehicule(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    modele = Column(String(100))
    annee_fabrication = Column(Integer)

class Voiture(Vehicule):
    __tablename__ = 'voiture'

    nb_porte = Column(Integer)

    id_marque_lookup = Column(Integer, ForeignKey('marque_lookup.id'))
    marque = relationship('MarqueLookup')

    roues = relationship("Roue", secondary='voiture_roue')

class VoitureRoue(Base):
    __tablename__ = 'voiture_roue'
    id_voiture = Column(Integer,  ForeignKey('voiture.id'), primary_key=True)
    id_roue = Column(Integer, ForeignKey('roue.id'), primary_key=True)
    date_installation = Column(Date, nullable=False)

    voiture = relationship('Voiture', backref=backref('roues'))
    roue = relationship('Roue', backref=backref('voitures'))
