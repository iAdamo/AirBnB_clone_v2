#!/usr/bin/python3
""" DBStorage Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new DBStorage instance and creates the engine.
        """
        try:
            self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
            if getenv('HBNB_ENV') == 'test':
                Base.metadata.drop_all(self.__engine)
        except Exception as e:
            print("Error creating engine:", str(e))

        if getenv('HBNB_ENV') == 'test':
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries the current database session for all objects of the given class

        Args:
            cls (BaseModel, optional): The class to query. Defaults to None.

        Returns:
            list: A list of all objects of the given class.
        """

        cls_list = [User, State, City, Amenity, Place, Review]
        if cls is None:
            obj_id = {}
            for cls in cls_list:
                try:
                    cls_table = self.__session.query(cls)
                except BaseException:
                    continue
                for row in cls_table:
                    key = f"{row.__class__.__name__}.{row.id}"
                    obj_id[key] = row
        else:
            cls_table = self.__session.query(cls)
            obj_id = {}
            for row in cls_table:
                key = f"{row.__class__.__name__}.{row.id}"
                obj_id[key] = row
        return obj_id

    def new(self, obj):
        """Adds the object to the current database session.

        Args:
            obj (BaseModel): The object to add.
        """
        try:
            self.__session.add(obj)
        except Exception as e:
            print("Error adding object to session:", str(e))

    def save(self):
        """Commits all changes of the current database session.
        """
        try:
            self.__session.commit()
        except Exception as e:
            print("Error committing to database:", str(e))

    def delete(self, obj=None):
        """
        Deletes obj from the current database session if not None.

        Args:
            obj (BaseModel, optional): The object to delete. Defaults to None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Method to create the current database session"""
        try:
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(session_factory)
            self.__session = Session()
        except Exception as e:
            print("Error creating tables:", str(e))

    def close(self):
        """Method to close the current database session
        """
        self.__session.close()
