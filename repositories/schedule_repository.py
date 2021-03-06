from db.run_sql import run_sql
from models.schedule import Schedule
from models.gym_class import Class
import repositories.member_repository as member_repo
import repositories.class_repository as class_repo


# Saves booking to database
def save(booking):
    if booking.gym_class.fully_booked == False:
        sql = "INSERT INTO schedule (member_id, class_id) VALUES (%s, %s) RETURNING id"
        values = [booking.member.id, booking.gym_class.id]
        results = run_sql(sql, values)
        booking.id = results[0]['id']
        return booking


# Save function again, but based on parameters being member and class IDs
def save_by_id(member_id, class_id):
    sql = "INSERT INTO schedule (member_id, class_id) VALUES (%s, %s) RETURNING id"
    values = member_id, class_id
    results = run_sql(sql, values)
    booking = results[0]['id']
    return booking


# Selects all items in schedule table
def select_all():
    schedule = []
    sql = "SELECT * FROM schedule"
    results = run_sql(sql)

    for row in results:
        member = member_repo.select(row['member_id'])
        gym_class = class_repo.select(row['class_id'])
        gym = Schedule(member, gym_class)
        schedule.append(gym)
    return schedule


# Finds all classes booked for member

# pdb.set_trace()

def classes(member):
    classes = []
    sql = "SELECT classes.* FROM classes INNER JOIN schedule ON schedule.class_id = classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = Class(row['name'], row['date'], row['time'], row['duration'], row['id'])
        classes.append(gym_class)
    return classes