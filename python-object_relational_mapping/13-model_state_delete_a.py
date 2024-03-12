#!/usr/bin/python3
'''
    13-model_state_delete_a.py
    Description: Deletes all State objects with a
    name containing the letter a from the database
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

    # Query and delete State objects with a name containing letter 'a'
    session.query(State).filter(State.name.like('%a%')).delete()

    # Commit transaction
    session.commit()

    session.close()
