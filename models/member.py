class Member:
    def __init__(self, first_name, second_name, phone_no, active = True, id = None):
        self.first_name = first_name
        self.second_name = second_name
        self.phone_no = phone_no
        self.active = active
        self.id = id

    def inactive(self):
        self.active = False