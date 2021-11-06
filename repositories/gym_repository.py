from db.run_sql import run_sql
from models.gym import Gym
import repositories.member_repository as member_repo
import repositories.class_repository as class_repo

def save(gym):
    sql = "INSERT INTO schedule (class_id, member_id) VALUES (%s, %s) RETURNING id"
    values = [gym.gym_class.id, gym.member.id]
    results = run_sql(sql, values)
    gym.id = results[0]['id']
    return gym

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