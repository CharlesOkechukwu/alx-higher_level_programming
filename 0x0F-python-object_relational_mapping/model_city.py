#!/usr/bin/python3
"""Module to create City class that inherits
from the Base class
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class that inherits from Base class
    attributes:
    __tablename__ : the tables name
    id : primary key
    name: name of the state
    state_id: a foreign key
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
