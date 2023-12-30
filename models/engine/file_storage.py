#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone
"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            new_obj = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    new_obj[key] = value
            return new_obj
        else:
            return FileStorage.__objects

    def new(self, obj):
        """sets in __objects (the obj) with key `<obj class name>.id`
        """
        key = '{}.{}'.format(obj.__class__.__name__, str(obj.id))
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file `(path: __file_path)`
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it's inside - if obj is equal to None,

        Args:
            obj (_type_, optional): class obj.
        """
        if obj:
            for obj_id, value in FileStorage.__objects.items():
                if value == obj:
                    del FileStorage.__objects[obj_id]
                    FileStorage().save()
                    break

    def close(self):
        """close method
        """
        self.reload()
