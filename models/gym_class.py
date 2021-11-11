class Class:
    def __init__(self, name, date, time, duration, fully_booked = False, id = None):
        self.name = name
        self.date = date
        self.time = time
        self.duration = duration
        self.fully_booked = fully_booked
        self.id = id
    

    # These methods allow 'fully_booked' to be toggled

    def class_full(self):
        self.fully_booked = True
        
    def class_available(self):
        self.fully_booked = False