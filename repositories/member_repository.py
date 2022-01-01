from db.run_sql import run_sql
from models.member import Member
from models.gym_class import Class
# import pdb

# Saves member to the database
def save(member):
    sql = "INSERT INTO members (first_name, second_name, phone_no, active) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.second_name, member.phone_no, member.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member


# Select all members (including inactive)
def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['second_name'], row['phone_no'], row['active'], row['id'])
        members.append(member)
    return members


# Selects member by ID
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['second_name'], result['phone_no'], result['active'], result['id'])
    return member


# Saves changes to an existing member
def update(member):
    sql = "UPDATE members SET(first_name, second_name, phone_no, active) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.second_name, member.phone_no, member.active, member.id]
    run_sql(sql, values)


# Selects active members and ignores inactive ones
def select_active_members():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['second_name'], row['phone_no'], row['active'], row['id'])
        if member.active == True:
            members.append(member)
    return members


# Selects inactive members and ignores active ones
def select_inactive_members():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['second_name'], row['phone_no'], row['active'], row['id'])
        if member.active == False:
            members.append(member)
    return members


# Finds all classes booked for member

# pdb.set_trace()

def classes(member):
    classes = []
    sql = "SELECT classes.* FROM classes INNER JOIN schedule ON schedule.class_id = classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = Class(row['name'], row['date'], row['time'], row['duration'], row['fully_booked'], row['id'])
        classes.append(gym_class)
    return classes