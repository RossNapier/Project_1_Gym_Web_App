import unittest
from models.gym_class import Class

class TestClass(unittest.TestCase):

    def setUp(self):
        self.test_class = Class("HIIT", "13/11/21", 18.00, 30)

    def test_class_has_name(self):
        self.assertEqual("HIIT", self.test_class.name)
    
    def test_class_has_date(self):
        self.assertEqual("13/11/21", self.test_class.date)
    
    def test_class_has_time(self):
        self.assertEqual(18.00, self.test_class.time)
    
    def test_class_has_duration(self):
        self.assertEqual(30, self.test_class.duration)
    
    def test_class_has_id(self):
        self.assertEqual(None, self.test_class.id)