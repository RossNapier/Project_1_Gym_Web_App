import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.test_member = Member("Steve", "Rogers", "0131 374 7474")

    def test_member_has_first_name(self):
        self.assertEqual("Steve", self.test_member.first_name)
    
    def test_member_has_second_name(self):
        self.assertEqual("Rogers", self.test_member.second_name)

    def test_member_has_phone_number(self):
        self.assertEqual("0131 374 7474", self.test_member.phone_no)

    def test_member_has_id(self):
        self.assertEqual(None, self.test_member.id)