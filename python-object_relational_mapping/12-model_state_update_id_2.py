#!/usr/bin/python3
'''
    12-model_state_update_id_2.py

    Description: Changes the name of a State
    object from the database hbtn_0e_6_usa
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

    # Query State object with id=2
    state_update = session.query(State).filter_by(id=2).first()

    # Update name of State obj
    state_update.name = "New Mexico"

    # Commit transaction
    session.commit()

    session.close()
