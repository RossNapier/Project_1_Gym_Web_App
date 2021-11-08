import pdb
from models.schedule import Schedule
from models.gym_class import Class
from models.member import Member

import repositories.member_repository as member_repo
import repositories.class_repository as class_repo
import repositories.schedule_repository as schedule_repo


member1 = Member("Steve", "Rogers", "0131 234 3544")
member2 = Member("Peter", "Parker", "0131 564 4332")
member3 = Member("Natasha", "Romanoff", "0131 221 3454")

member_repo.save(member1)
member_repo.save(member2)
member_repo.save(member3)

class1 = Class("HIIT", "13/11/21", "18.00", 30)
class2 = Class("Boxing", "15/11/21", "20.00", 45)
class3 = Class("Yoga", "18/11/21", "06.00", 60)
class4 = Class("Cycle", "19/11/21", "06.00", 30)

class_repo.save(class1)
class_repo.save(class2)
class_repo.save(class3)
class_repo.save(class4)

booking1 = Schedule(member1, class1)
schedule_repo.save(booking1)

# pdb.set_trace()