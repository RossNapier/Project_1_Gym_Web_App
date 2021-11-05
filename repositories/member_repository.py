from db.run_sql import run_sql

from models.gym_class import Class
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, second_name, phone_no) VALUES (%s, %s, %s) RETURNING *"
    values = [member.first_name, member.second_name, member.phone_no]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['second_name'], row['phone_no'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['second_name'], result['phone_no'], result['id'])
    return member