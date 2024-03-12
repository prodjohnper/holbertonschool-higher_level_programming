#!/usr/bin/python3
'''
    9-model_state_filter_a.py
    Description: Lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa
'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create and bind SQLAlchemy engine to session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to select all State objects containing the letter 'a'
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
