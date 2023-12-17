#!/usr/bin/python3
"""Module to create state class that inherits
from the Base class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State class that inherits from Base class
    attributes:
    __tablename__ : the tables name
    id : primary key
    name: name of the state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
