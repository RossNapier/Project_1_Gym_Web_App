from db.run_sql import run_sql
from models.gym_class import Class

def save(gym_class):
    sql = "INSERT INTO classes (name, date, time, duration) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [gym_class.name, gym_class.date, gym_class.time, gym_class.duration]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_class.id = id
    return gym_class

def select_all():
    classes = []
    sql = "SELECT * FROM classes"
    results = run_sql(sql)

    for row in results:
        gym_class = Class(row['name'], row['date'], row['time'], row['duration'], row['id'])
        classes.append(gym_class)
    return classes

def select(id):
    gym_class = None
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Class(result['name'], result['date'], result['time'], result['duration'], result['id'])
    return gym_class

def update(gym_class):
    sql = "UPDATE classes SET(name, date, time, duration) = (%s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, gym_class.date, gym_class.time, gym_class.duration, gym_class.id]
    run_sql(sql, values)