#!/usr/bin/python3
"""Defines a City class"""


from sqlalchemy import Column, ForeignKey, Integer, String

from relationship_state import Base, State


class City(Base):
    """City class to represent a city in a database.

    Attributes:
        __tablename__ (str): The name of the database table for cities.
        id (int): The unique identifier for the city.
        name (str): The name of the city (up to 128 characters).
        state_id (int): The foreign key referencing the state to which the city belongs.
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
