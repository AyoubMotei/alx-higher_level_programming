#!/usr/bin/python3
"""Defines a State class"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class to represent a state in a database.

    Attributes:
        __tablename__ (str): The name of the database table for states.
        id (int): The unique identifier for the state.
        name (str): The name of the state (up to 128 characters).
        cities (relationship): A relationship to the City class, allowing navigation from state to its cities.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
