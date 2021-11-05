from db.run_sql import run_sql
from models.gym import Gym
import repositories.member_repository as member_repo
import repositories.class_repository as class_repo

def save(gym_class):
    sql = "INSERT INTO classes (name, date, time, duration) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [gym_class.name, gym_class.date, gym_class.time, gym_class.duration]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_class.id = id
    return gym_class

def select_all():
    schedule = []
    sql = "SELECT * FROM classes"
    results = run_sql(sql)

    for row in results:
        member = member_repo.select(row['member_id'])
        gym_class = class_repo.select(row['class_id'])
        gym = Gym(member, gym_class, row['id'])
        schedule.append(gym)
    return schedule