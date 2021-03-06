from db.run_sql import run_sql
from models.gym_class import Class
from models.member import Member


# Saves details to the database - for new instances only
def save(gym_class):
    sql = "INSERT INTO classes (name, date, time, duration, fully_booked) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [gym_class.name, gym_class.date, gym_class.time, gym_class.duration, gym_class.fully_booked]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_class.id = id
    return gym_class


# Selects all gym_classes (even if fully booked)
def select_all():
    classes = []
    sql = "SELECT * FROM classes"
    results = run_sql(sql)

    for row in results:
        gym_class = Class(row['name'], row['date'], row['time'], row['duration'], row['fully_booked'], row['id'])
        classes.append(gym_class)
    return classes


# Selects one gym_class by ID
def select(id):
    gym_class = None
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Class(result['name'], result['date'], result['time'], result['duration'], result['fully_booked'], result['id'])
    return gym_class


# Updates gym_class details (so like Save but for existing instance)
def update(gym_class):
    sql = "UPDATE classes SET(name, date, time, duration, fully_booked) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, gym_class.date, gym_class.time, gym_class.duration, gym_class.fully_booked, gym_class.id]
    run_sql(sql, values)


# Finds all members booked into particular gym_class
def members(gym_class):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN schedule ON schedule.member_id = members.id WHERE class_id = %s"
    values = [gym_class.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['second_name'], row['phone_no'], row['active'], row['id'])
        if member.active == True:   
            members.append(member)
    return members


# Checks if certain class is available
def check_class(gym_class):
    if len(members(gym_class)) > 8:
        Class.class_full(gym_class)
        update(gym_class)


# Checks all classes to see if they are now available (ie. if an attendee becomes inactive)
def check_all_classes():
    classes = select_all()
    for gym_class in classes:
        if len(members(gym_class)) > 8:
            Class.class_full(gym_class)
            update(gym_class)
        else:
            Class.class_available(gym_class)
            update(gym_class)


# Selects only available classes - booked classes are ignored
def select_available_classes():
    classes = []
    sql = "SELECT * FROM classes"
    results = run_sql(sql)

    for row in results:
        gym_class = Class(row['name'], row['date'], row['time'], row['duration'], row['fully_booked'], row['id'])
        if gym_class.fully_booked == False:   
            classes.append(gym_class)
    return classes
