#!/usr/bin/python3
"""Prints the first 'State' object from the database 'hbtn_0e_6_usa'."""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as av

if __name__ == "__main__":
    url_db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(av[1], av[2], av[3])
    engine = create_engine(url_db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%"))
    [print("{}: {}".format(s.id, s.name)) for s in states]
