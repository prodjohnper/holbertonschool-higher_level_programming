#!/usr/bin/python3
'''
    model_state.py
    
    Description: Class State that inherits from Base
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''
        State Class that inherits from Base
    '''
    __tablename__ = 'states'

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
