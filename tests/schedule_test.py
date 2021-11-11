import unittest
from models.schedule import Schedule
from models.gym_class import Class
from models.member import Member


class TestSchedule(unittest.TestCase):

    def setUp(self):
        member = Member("Steve", "Rogers", "0131 374 7474")
        gym_class = Class("HIIT", "13/11/21", 18.00, 30)
        self.test_gym = Schedule(member, gym_class)

    def test_schedule_member_has_first_name(self):
        self.assertEqual("Steve", self.test_gym.member.first_name)
    
    def test_schedule_member_has_second_name(self):
        self.assertEqual("Rogers", self.test_gym.member.second_name)
    
    def test_schedule_member_has_phone_no(self):
        self.assertEqual("0131 374 7474", self.test_gym.member.phone_no)
    
    def test_schedule_member_has_id(self):
        self.assertEqual(None, self.test_gym.member.id)

    def test_schedule_gym_class_has_name(self):
        self.assertEqual("HIIT", self.test_gym.gym_class.name)
    
    def test_schedule_gym_class_has_date(self):
        self.assertEqual("13/11/21", self.test_gym.gym_class.date)
    
    def test_schedule_gym_class_has_time(self):
        self.assertEqual(18.00, self.test_gym.gym_class.time)
    
    def test_schedule_gym_class_has_duration(self):
        self.assertEqual(30, self.test_gym.gym_class.duration)
    
    def test_schedule_gym_class_has_id(self):
        self.assertEqual(None, self.test_gym.gym_class.id)
    