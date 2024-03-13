#!/usr/bin/python3
'''
    model_city.py

    Description: Class City that inherits from Base
'''
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''
        City class that inherits from Base
    '''
    __tablename__ = 'cities'

    id = Column(
        Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True
    )

    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
