#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ The state class, contains name attribute """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City',
            backref='state',
            cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id"""
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]
