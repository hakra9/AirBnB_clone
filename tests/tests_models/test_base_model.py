#!/usr/bin/python3
"""
Defines tests for the basemodel classs the parent class for
the AiBnB project
Unitests calsses:
    TestBaseModel_instantiation
"""
from time import sleep
import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel_instantiation(unittest.TestCase):
    """testing all objects of the class"""

    def test_typeclass(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_instance(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_instance(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_instance(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_kwrags(self):
        date = datetime.now()
        date = date.isoformat()
        obj = BaseModel(id="1234567", created_at=date, updated_at=date)
        self.assertEqual(obj.id, "1234567")
        self.assertEqual(obj.updated_at, date)
        self.assertEqual(obj.created_at, date)

    def test_time_effiecency(self):
        obj1 = BaseModel()
        sleep(1)
        obj2 = BaseModel()
        self.assertGreater(obj2.created_at, obj1.created_at)

    def test_str_format(self):
        dt = datetime.now().isoformat()
        obj = BaseModel(id="123", created_at=dt, updated_at=dt)
        str_format = obj.__str__()
        self.assertIn("[BaseModel] (123)", str_format)
        self.assertIn("'id': '123'", str_format)
        self.assertIn("'created_at: '" + dt, str_format)
        self.assertIn("'updated_at: '" + dt, str_format)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class TestBaseModel_save(unittest.TestCase):
    """testing the save """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_checking_date_update(self):
        obj = BaseModel()
        self.assertEqual(obj.created_at, obj.updated_at)
        sleep(0.05)
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_save_with_arg(self):
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.save(None)

    def test_saved_objects(self):
        obj = BaseModel()
        obj.save()
        with open("file.json", 'r') as file:
            self.assertIn("BaseModel." + obj.id, file.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """testing the conveted object to a dictionary function (to_dict)"""

    def setUp(self):
        obj = BaseModel()
        dic = obj.to_dict()
        self.dic = dic
        self.obj = obj

    def test_return_type(self):
        self.assertEqual(dict, type(self.dic))

    def test_date_type(self):
        self.assertEqual(str, self.dic["created_at"])
        self.assertEqual(str, self.dic["updated_at"])

    def test_dict_keys(self):
        self.assertIn("id", self.dic)
        self.assertIn("created_at", self.dic)
        self.assertIn("updated_at", self.dic)
        self.assertIn("__class__", self.dic)

    def test_dict_values(self):
        self.obj.name = "Amr"
        self.obj.number = 142
        self.assertEqual(self.dic["name"], "Amr")
        self.assertEqual(self.dic["number"], 142)

    def test_contrast_to_dict(self):
        self.assertNotEqual(self.obj.__dict__, self.dic)

    def test_none_args(self):
        obj2 = BaseModel()
        with self.assertRaises(TypeError):
            obj2.to_dict(None)


if __name__ == "__main__":
    unittest.main()
