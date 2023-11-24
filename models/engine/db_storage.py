#!/usr/bin/python3
""" DBStorage Module for HBNB project """

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database.
    """
    __engine = None
    __session = None
    
    def __init__(self):
        """Initializes a new DBStorage instance and creates the engine.
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'), 
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    
    def all(self, cls=None):
        """
        Queries the current database session for all objects of the given class.

        Args:
            cls (BaseModel, optional): The class to query. Defaults to None.

        Returns:
            list: A list of all objects of the given class.
        """
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if cls is None:
            cls_list = [User, State, City, Amenity, Place, Review]
            obj_id = {}
            for cls in cls_list:
                cls_table = DBStorage.__session.query(cls).all()
                for row in cls_table:
                    key = f"{row.__class__.__name__}.{row.id}"
                    obj_id[key] = row
        else:
            cls_table = DBStorage.__session.query(cls).all()
            obj_id = {}
            for row in cls_table:
                key = f"{row.__class__.__name__}.{row.id}"
                obj_id[key] = row
            print("obj_id: ", obj_id)
        return obj_id
    
    def new(self, obj):
        """Adds the object to the current database session.

        Args:
            obj (BaseModel): The object to add.
        """
        DBStorage.__session.add(obj)
    
    def save(self):
        """Commits all changes of the current database session.
        """
        DBStorage.__session.commit()
    
    def delete(self, obj=None):
        """
        Deletes obj from the current database session if not None.

        Args:
            obj (BaseModel, optional): The object to delete. Defaults to None.
        """
        if obj is not None:
            DBStorage.__session.delete(obj)
            
    def reload(self):
        """Creates all tables in the database and initializes the session.
        """
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()
    
    def close(self):
        """public methodto to call remove method"""
        DBStorage.__session.close()
