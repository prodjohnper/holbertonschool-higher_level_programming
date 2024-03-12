#!/usr/bin/python3
'''
    11-model_state_insert.py

    Description: Adds State object “Louisiana” to the database hbtn_0e_6_usa
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

    # Create all tables defined in Base
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")  # Create State object
    session.add(new_state)  # Add new obj to session

    # Commit transaction
    session.commit()

    print(new_state.id)

    session.close()
