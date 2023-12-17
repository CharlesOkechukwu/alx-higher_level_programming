#!/usr/bin/python3
"""module to select all cities and states"""
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """select all cities and states using sql alchemy
    must not execute when imported
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    sql_query = session.query(City, State).join(State).order_by(City.id)
    for city, state in sql_query.all():
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))
