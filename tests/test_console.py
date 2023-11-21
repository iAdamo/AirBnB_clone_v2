#!/usr/bin/python3
""" test for console
"""
import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cli = HBNBCommand()

    def test_prompt(self):
        self.assertEqual(self.cli.prompt, '(hbnb) ')

    def test_classes(self):
        self.assertIn('BaseModel', self.cli.classes)
        self.assertIn('User', self.cli.classes)
        self.assertIn('Place', self.cli.classes)
        self.assertIn('State', self.cli.classes)
        self.assertIn('City', self.cli.classes)
        self.assertIn('Amenity', self.cli.classes)
        self.assertIn('Review', self.cli.classes)

    def test_dot_cmds(self):
        self.assertIn('all', self.cli.dot_cmds)
        self.assertIn('count', self.cli.dot_cmds)
        self.assertIn('show', self.cli.dot_cmds)
        self.assertIn('destroy', self.cli.dot_cmds)
        self.assertIn('update', self.cli.dot_cmds)

    def test_types(self):
        self.assertIn('number_rooms', self.cli.types)
        self.assertIn('number_bathrooms', self.cli.types)
        self.assertIn('max_guest', self.cli.types)
        self.assertIn('price_by_night', self.cli.types)
        self.assertIn('latitude', self.cli.types)
        self.assertIn('longitude', self.cli.types)

    def test_do_quit(self):
        with self.assertRaises(SystemExit):
            self.cli.do_quit('')

    def test_do_EOF(self):
        with self.assertRaises(SystemExit):
            self.cli.do_EOF('')

    def test_emptyline(self):
        self.assertIsNone(self.cli.emptyline())

    def test_do_show(self):
        self.cli.do_create('BaseModel')
        obj = list(storage.all().values())[0]
        self.cli.do_show('BaseModel ' + obj.id)

    def test_do_destroy(self):
        self.cli.do_create('BaseModel')
        obj = list(storage.all().values())[0]
        self.cli.do_destroy('BaseModel ' + obj.id)
        self.assertNotIn('BaseModel.' + obj.id, storage.all())

    def test_do_all(self):
        self.cli.do_create('BaseModel')
        self.cli.do_all('BaseModel')

    def test_do_update(self):
        self.cli.do_create('BaseModel')
        obj = list(storage.all().values())[0]
        self.cli.do_update('BaseModel ' + obj.id + ' name "John"')
        self.assertEqual(obj.name, 'John')


if __name__ == '__main__':
    unittest.main()
