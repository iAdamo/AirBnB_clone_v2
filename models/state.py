#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models

class State(BaseModel, Base):
    """ The state class, contains name attribute """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    from models.engine.db_storage import DBStorage
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id
        """
        city_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
