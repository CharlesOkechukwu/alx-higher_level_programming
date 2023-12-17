#!/usr/bin/python3
"""module to select states that start with a"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """select states that start with a using sql alchemy
    must not execute when imported
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter(
            State.name.contains('a')).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
