import pdb
from models.schedule import Schedule
from models.gym_class import Class
from models.member import Member

import repositories.member_repository as member_repo
import repositories.class_repository as class_repo
import repositories.schedule_repository as schedule_repo


# Seeding database with members

member1 = Member("Steve", "Rogers", "07586 303022")
member2 = Member("Tony", "Stark", "07868 391910")
member3 = Member("Natasha", "Romanoff", "07594 030029")
member4 = Member("Pepper", "Potts", "07982 392938")
member5 = Member("Steven", "Strange", "07352 182818")
member6 = Member("Peter", "Parker", "07691 092991")
member7 = Member("Bruce", "Banner", "07482 238818")
member8 = Member("Carol", "Danvers", "07493 1048282")
member9 = Member("Janet", "Van Dyne", "07949 929299")
member_repo.save(member1)
member_repo.save(member2)
member_repo.save(member3)
member_repo.save(member4)
member_repo.save(member5)
member_repo.save(member6)
member_repo.save(member7)
member_repo.save(member8)
member_repo.save(member9)


# Seeding databse with classes

class1 = Class("HIIT", "13/11/21", "18.00", 30)
class2 = Class("Boxing", "15/11/21", "20.00", 45)
class3 = Class("Yoga", "18/11/21", "08.00", 60)
class4 = Class("Spin", "19/11/21", "06.00", 30)
class_repo.save(class1)
class_repo.save(class2)
class_repo.save(class3)
class_repo.save(class4)


# Seeding database with bookings (ie. add to schedule table)

booking1 = Schedule(member1, class1)
schedule_repo.save(booking1)
booking2 = Schedule(member2, class1)
schedule_repo.save(booking2)
booking3 = Schedule(member3, class1)
schedule_repo.save(booking3)
booking4 = Schedule(member4, class1)
schedule_repo.save(booking4)
booking5 = Schedule(member5, class1)
schedule_repo.save(booking5)
booking6 = Schedule(member6, class1)
schedule_repo.save(booking6)
booking7 = Schedule(member7, class1)
schedule_repo.save(booking7)
booking8 = Schedule(member8, class1)
schedule_repo.save(booking8)
booking10 = Schedule(member6, class2)
schedule_repo.save(booking10)
booking11 = Schedule(member7, class2)
schedule_repo.save(booking11)
booking12 = Schedule(member8, class2)
schedule_repo.save(booking12)
booking13 = Schedule(member1, class3)
schedule_repo.save(booking13)
booking14 = Schedule(member2, class3)
schedule_repo.save(booking14)
booking15 = Schedule(member3, class4)
schedule_repo.save(booking15)
booking16 = Schedule(member4, class4)
schedule_repo.save(booking16)
booking17 = Schedule(member5, class4)
schedule_repo.save(booking17)
