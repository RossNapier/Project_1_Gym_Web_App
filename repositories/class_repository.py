from db.run_sql import run_sql

from models.gym_class import Class
from models.member import Member

def save(gym_class):
    sql = "INSERT INTO classes (name, date, time, duration) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [gym_class.name, gym_class.date, gym_class.time, gym_class.duration]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_class.id = id
    return gym_class