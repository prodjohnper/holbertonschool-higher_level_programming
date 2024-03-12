#!/usr/bin/python3
'''
    10-model_state_my_get.py
    Description: Prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create and bind SQLAlchemy engine to session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to select the State object with state name
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print('Not found')

    session.close()
