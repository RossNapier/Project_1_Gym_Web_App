from db.run_sql import run_sql
from models.schedule import Schedule
import repositories.member_repository as member_repo
import repositories.class_repository as class_repo

def save(booking):
    sql = "INSERT INTO schedule (class_id, member_id) VALUES (%s, %s) RETURNING id"
    values = [booking.gym_class.id, booking.member.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

def select_all():
    schedule = []
    sql = "SELECT * FROM classes"
    results = run_sql(sql)

    for row in results:
        member = member_repo.select(row['member_id'])
        gym_class = class_repo.select(row['class_id'])
        gym = Schedule(member, gym_class, row['id'])
        schedule.append(gym)
    return schedule