import unittest
from models.gym import Gym

class TestGym(unittest.TestCase):

    def setUp(self):
        self.test_gym = Gym("Leith Gym", "123 Leith Walk, Edinburgh EH6 6LK", "0131 384 5834")

    def test_gym_has_name(self):
        self.assertEqual("Leith Gym", self.test_gym.name)
    
    def test_gym_has_address(self):
        self.assertEqual("123 Leith Walk, Edinburgh EH6 6LK", self.test_gym.address)
    
    def test_gym_has_phone_no(self):
        self.assertEqual("0131 384 5834", self.test_gym.phone_no)
    
    def test_gym_has_id(self):
        self.assertEqual(None, self.test_gym.id)