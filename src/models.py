import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,)
    username = Column(String(20), unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String(12), unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    gender = Column(String (2))


    __table_args__ = (
        UniqueConstraint('email', 'username', 'password'),
    )



class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String (2))

class FavoriteCharacters(Base):
    __tablename__ = 'FavoriteCharacters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name_character = Column(Integer, ForeignKey('characters.id'))
    user = relationship(User)
    characters = relationship(Characters)


    

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    weather = Column(String(10))
    name = Column(String)
    diameter = Column(Integer)


class FavoritePlanets(Base):
    __tablename__ = 'FavoritePlanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name_planet = Column(Integer, ForeignKey('planets.id'))
    user = relationship(User)
    planets = relationship(Planet)
    

class Starship(Base):
    __tablename__ = 'Starships'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    passangers = Column(Integer)

class FavoriteStarships(Base):
    __tablename__ = 'FavoriteStarships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name_starship = Column(Integer, ForeignKey('Starships.id'))
    user = relationship(User)
    starships = relationship(Starship)

class Film(Base):
    __tablename__ = 'Films'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    Director = Column(String)
    Producer = Column(String)

class FavoriteFilms(Base):
    __tablename__ = 'FavoriteFilms'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name_film = Column(Integer, ForeignKey('Films.id'))
    user = relationship(User)
    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')