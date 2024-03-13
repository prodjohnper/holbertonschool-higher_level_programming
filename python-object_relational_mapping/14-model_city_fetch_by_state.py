#!/usr/bin/python3
'''
    14-model_city_fetch_by_state.py

    Description: Prints all City objects from the database hbtn_0e_14_usa
'''
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create and bind SQLAlchemy engine to session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True)

    # Create all tables defined in Base
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to select all City objects
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State).filter_by(
            id=city.state_id).first().name
        print(f'{state_name}: ({city.id}) {city.name}')

    session.close()
